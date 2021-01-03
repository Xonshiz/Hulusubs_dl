#!/usr/bin/env python
# -*- coding: utf-8 -*-

from cust_utils import *
import subtitle_processing
from api import *
import os
import re


class Hulu:
    def __init__(self, url, cookie_value, language, extension, download_location, cwd):
        print("Class Instantiated")
        if "/series/" in url:
            self.show_link(url, cookie_value, language, extension, download_location)
        elif "/watch/" in url:
            self.episode_link(url, cookie_value, language, extension, download_location)
        else:
            raise Warning("URL Not Supported")

    def episode_link(self, url, cookie_value, language, extension, download_location):
        transcript_urls = {}
        eab_id = str(url).split('/watch/')[-1].replace('/', '')
        eab_id_information = hulu_api.get_full_eab_id(eab_id, cookie_value)
        eab_id = dict(eab_id_information).get('eab_id', None)
        if not eab_id:
            print("You seem to be out of USA. Use a VPN.")
            return False
        payload = utils.get_playlist_body(eab_id=eab_id)
        if payload:
            print(payload)
            # Logic to find the URL for the language and extension provided and download it.
            playlist_info = hulu_api.get_playlist_information(payload, cookie_value)
            if playlist_info:
                playlist_info = dict(playlist_info)
                transcripts = playlist_info.get('transcripts_urls', None)
                if not transcripts:
                    print("Couldn't Find Transcript URLs. Exiting.")
                    return False
                else:
                    transcript_urls = dict(transcripts)
                    # we will convert webvtt to any other subtitle format.So,we'll use that URL to get subtitle content.
                    if extension not in utils.DEFAULT_SUB_EXT:
                        transcript_urls[extension] = transcript_urls.get('webvtt', {})
                    video_metadata = dict(hulu_api.get_eab_id_metadata(eab_id, cookie_value, language)).get('items', {})
                    video_metadata = dict(list(video_metadata)[0])
                    series_name = video_metadata.get('series_name', "No Name Found")
                    season_number = video_metadata.get('season', "01")
                    episode_number = video_metadata.get('number', "01")
                    file_name = '{0} - S{1}E{2} [{3} Sub].{4}'.format(series_name, season_number, episode_number, language, extension)
                    selected_extension = transcript_urls.get(extension, None)
                    if not selected_extension:
                        print("Couldn't Find {0} In Hulu".format(extension))
                    else:
                        url = str(dict(selected_extension).get(language, None)).strip()
                        subtitle_content = browser_instance.get_request(url, cookie_value, text_only=True)
                        path_created = path_util.create_paths(download_location + os.sep + series_name + os.sep + season_number)
                        if path_created:
                            if extension == 'srt':
                                subtitle_content = subtitle_processing.convert_vtt_to_srt(subtitle_content)
                            elif extension == 'ass':
                                subtitle_content = subtitle_processing.convert_vtt_to_ass(subtitle_content)
                            file_written = utils.create_file_binary_mode(path_created, os.sep + file_name, subtitle_content)
                            if file_written:
                                return True
                            else:
                                return False
        else:
            print("Failed To Retrieve The Data.")
        return None

    def show_link(self, url, cookie_value, language, extension, download_location):
        eab_id_matches = re.findall(r'-([0-9A-Za-z]+)', str(url).split('/series/')[-1])
        if eab_id_matches and len(eab_id_matches) > 1:
            eab_id_matches.pop(0)
            eab_id = 'EAB::' + '-'.join(eab_id_matches)
            series_metadata = dict(hulu_api.get_eab_id_metadata(eab_id, cookie_value, language)).get('items', {})
            season_numbers = []
            season_episodes = []
            if not series_metadata:
                print("No Series Information Found. Make sure you're in USA IP.")
                return False
            for item in series_metadata:
                # Saving the season numbers
                season_numbers.append(dict(item).get('season', 0))
            for season in season_numbers:
                # For every season, we'll collect EAB IDs of the episodes.
                season_metadata = dict(hulu_api.get_series_season_metadata(eab_id, cookie_value, season)).get('items', {})
                for season_item in season_metadata:
                    season_episodes.append(dict(season_item).get('id', None))
            for episode_eab in season_episodes:
                if episode_eab:
                    self.episode_link('https://www.hulu.com/watch/{0}'.format(episode_eab), cookie_value, language, extension, download_location)
        return True