#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import re
import cfscrape
import requests
import json
import os
from bs4 import BeautifulSoup


class HuluSubs:
    def __init__(self, url, subtitle_type):
        self.url = url
        self.subtitle_format = subtitle_type
        hulu__episode__regex = r'^https?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/watch/)[\d]+'
        hulu__episode = re.match(hulu__episode__regex, self.url)

        if hulu__episode:
            self.single_episode(self.url)
            sys.exit(0)
        else:
            print("Please Check The URL again!")
            sys.exit(1)

    def page_downloader(self, page_url, **kwargs):
        headers = {
            'User-Agent':
                'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            'Accept-Encoding': 'gzip, deflate'
        }

        sess = requests.session()
        sess = cfscrape.create_scraper(sess)

        connection = sess.get(page_url, headers=headers, cookies=kwargs.get("cookies"))
        if connection.status_code != 200:
            print("Whoops! Seems like I can't connect to website.")
            print("It's showing : %s" % connection)
            print("Run this script with the --verbose argument and report the issue along with log file on Github.")
            sys.exit(1)
        else:
            page_source = BeautifulSoup(connection.content, "html.parser")  # text.encode("utf-8")
            connection_cookies = sess.cookies

            return page_source, connection_cookies

    def single_episode(self, url, **kwargs):
        page_source, cookies = self.page_downloader(page_url=url, cookies=kwargs.get("session_cookies"))

        data_json = json.loads(str(page_source.find_all('script', {'type': 'application/ld+json'})[0].text))

        series_name = data_json["partOfSeries"]["name"]
        episode_number = data_json["episodeNumber"]
        season_number = data_json["partOfSeason"]["seasonNumber"]
        con_id = str(re.search(r'/video/(.*?)\?', str(data_json["image"])).group(1)).strip()

        file_name = os.path.abspath("{0} - S0{1}E0{2}.vtt".format(series_name, season_number, episode_number))

        caption_url = "http://www.hulu.com/captions.xml?content_id=" + con_id
        xml_source, xml_cookies = self.page_downloader(page_url=caption_url, cookies=cookies)
        vtt_file_link = str(re.search(r'<en>(.*?)</en>', str(xml_source)).group(1)).replace('captions', 'captions_webvtt').replace('smi', 'vtt')

        smi_source, smi_cookies = self.page_downloader(page_url=vtt_file_link, cookies=xml_cookies)

        print("-" * len("Downloading %s - %s" % (series_name, episode_number)))
        print("Downloading %s - %s" % (series_name, episode_number))

        with open(file_name, "wb") as sub_file:
            sub_file.write(str(smi_source))

        if str(self.subtitle_format).lower() in ['srt']:
            print("Converting File")
            with open(file_name, 'r+') as read_file:
                """
                A HUGE thanks to fiskenslakt (https://www.reddit.com/user/fiskenslakt) for this "VTT" to "SRT
                conversion". Read his contribution here : https://www.reddit.com/r/learnpython/comments/4i380g/add_
                line_number_for_empty_lines_in_a_text_file/
                """
                lines = read_file.readlines()
                lines.pop()
                """
                Fix for SRT file. Remove the last '\n', so that it doesn't increase the line count
                and mess up the whole srt file.
                """

                new_line_count = 0
                for i, num in enumerate(lines):
                    if num == '\n':
                        new_line_count += 1
                        lines[i] = str(new_line_count)
                read_file.seek(0)

                for line in lines:
                    final_line = str(line).replace('WEBVTT\n','').replace("--&gt;", "-->").replace("</p></body></html>", "").replace(".", ",")
                    read_file.write(final_line + '\n')
            try:
                os.rename(file_name, str(file_name).replace(".vtt", ".srt"))
            except Exception as file_renaming_error:
                print("Couldn't convert file.")
                print(file_renaming_error)
                pass

        print("Download Complete For {0} - S0{1}E0{2}".format(series_name, season_number, episode_number))
        print("-"*len("Download Complete For {0} - S0{1}E0{2}".format(series_name, season_number, episode_number)))


if __name__ == '__main__':
    main_url = ""
    sub_type = ""

    if sys.version_info[:1] == (2,):
        main_url = str(raw_input('Enter a URL for hulu.com : ')).strip()
        sub_type = str(raw_input("Which format do you want? (SRT or VTT) : ")).strip()
    elif sys.version_info[:1] == (3,):
        main_url = str(input('Enter a URL for hulu.com : ')).strip()
        sub_type = str(input("Which format do you want? (SRT or VTT) : ")).strip()
    # mainurl = "https://www.hulu.com/watch/872899"
    # subType = "srt"

    print("")
    if not main_url:
        print("You did not provide me with a URL.")
        sys.exit()
    else:
        SubDownloader = HuluSubs(url=main_url, subtitle_type=sub_type)