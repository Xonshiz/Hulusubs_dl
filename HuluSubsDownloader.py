#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import absolute_import
from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import sys
import re
import cfscrape
import urllib.request


class HuluSubs(object):
    def __init__(self):
        self.url = mainurl
        self.subFormat = subType
        hulu_Episode_Regex = r'^http?://(?:(?P<prefix>www)\.)?(?P<url>hulu\.com/watch/)[\d]+'
        hulu_Episode = re.match(hulu_Episode_Regex, self.url)

        if hulu_Episode:
            self.singleEpisode(self.url)


    def singleEpisode(self, url):
        scraper = cfscrape.create_scraper()
        html_content = str(scraper.get(url).content)
        showTitle = str(re.search('og\:title\"\ content\=\"(.*?)\"\/\>', html_content).group(1)).strip()
        show_name = showTitle.split(':')[0]
        # print(show_name)
        episode_number = str(re.search('\"episodeNumber\"(.*?)\,', html_content).group(1)).replace(':','').replace('\\n','').strip()
        # print(episode_number)
        season_number = str(re.search('\"seasonNumber\"(.*?)\}', html_content).group(1)).replace(':', '').replace('\\n', '').strip()
        # print(season_number)
        fileName_special = str(show_name) + " - S0" + str(season_number) + "E0" + str(episode_number) # Top Lamb / Molly Molly Mouthful - S03E01
        # print(fileName_special)
        fileName = re.sub(r'[^A-Za-z0-9\ \-\' \\]+', '', fileName_special)
        # print(fileName)
        try:
            con_id = str(re.search('\/video\/(.*?)\?', html_content).group(1)).replace(':', '').replace('\\n','').strip()
        except Exception:
            print("Looks like the video is Hardsubbed!")
            sys.exit()
        captionLookup = 'http://www.hulu.com/captions.xml?content_id=' + str(con_id)

        linkVisitor = scraper.get(captionLookup).content
        # print(linkVisitor)
        vtt = str(re.search('\<en\>(.*?)\<\/en\>', str(linkVisitor)).group(1)).replace(': ', '').replace('\\n','').strip()
        vtt_link = str(vtt).replace('captions','captions_webvtt').replace('smi','vtt')
        # print(vtt_link)

        if str(self.subFormat).lower() in ['vtt']:
            print("Downloading %s - %s" % (show_name, episode_number))
            urllib.request.urlretrieve(vtt_link, fileName + '.vtt')
            sys.exit()
        elif str(self.subFormat).lower() in ['srt']:
            print("Downloading %s - %s" % (show_name, episode_number))
            urllib.request.urlretrieve(vtt_link, fileName + '.srt')
            with open(fileName + '.srt','r+') as f:  # A HUGE thanks to fiskenslakt (https://www.reddit.com/user/fiskenslakt) for this "VTT" to "SRT conversion". Read his contribution here : https://www.reddit.com/r/learnpython/comments/4i380g/add_line_number_for_empty_lines_in_a_text_file/
                lines = f.readlines()
                newLineCount = 0
                for i, num in enumerate(lines):
                    if num == '\n':
                        newLineCount += 1
                        lines[i] = str(newLineCount) + '\n'
                f.seek(0)
                for line in lines:
                    finalLine = str(line).replace('WEBVTT','').replace("--&gt;","-->").replace("</p></body></html>","")
                    f.write(finalLine + '\n')

        print("Downloaded %s - %s" % (show_name, episode_number))


if __name__ == '__main__':

    if sys.version_info[:1] == (2,):
        mainurl = str(raw_input('Enter a URL : ')).strip()
        subType = str(raw_input("Which format do you want : ")).strip()
    elif sys.version_info[:1] == (3,):
        mainurl = str(input('Enter a URL : ')).strip()
        subType = str(input("Which format do you want : ")).strip()

    if not mainurl:
        print("You did not provide me with a URL.")
        sys.exit()
    else:
        SubDownloader = HuluSubs()