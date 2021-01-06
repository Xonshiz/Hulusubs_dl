#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
from .cust_utils import *
from .__version__ import __version__
from .hulu import Hulu


class HuluSubsDl:
    def __init__(self, argv, cwd):
        cookie_file_name = '/.cookie'
        config_file_name = '/.config'
        supported_languages = ['en', 'es']
        supported_extensions = ['srt', 'vtt', 'smi', 'ttml']
        self.max_tries_for_cookie = 5
        cookie_file_data = None
        config_file_data = None
        url = None
        self.download_location = None
        self.subtitle_lang = None
        self.subtitle_extension = None
        self.proxy = []
        skip_config = False

        args = self.add_argparse()
        if args.version:
            print(__version__)
            sys.exit(0)
        if args.make_config:
            config_object = self.get_config_file_data()
            config_data = self.ask_config_file_data(config_object)
            file_written = utils.create_file(cwd, config_file_name, config_data)
            if not file_written:
                print("Couldn't write config file.")
            sys.exit(0)
        if args.hulu_url:
            url = args.hulu_url[0]
        else:
            while not url:
                url = input("Enter Hulu URL : ")
        url = url.strip()
        if args.skip_config:
            skip_config = args.skip_config[0]

        if not skip_config:
            print("Reading Configuration File.")
            if path_util.file_exists(cwd, config_file_name):
                config_file_data = eval(utils.read_file_data(cwd, config_file_name))
            else:
                # ask config data from user
                config_object = self.get_config_file_data()
                config_data = self.ask_config_file_data(config_object)
                file_written = utils.create_file(cwd, config_file_name, config_data)
                if file_written:
                    config_file_data = config_data
            if not config_file_data:
                print("Resetting Config File")
                config_file_data = self.get_config_file_data()
            else:
                self.set_config_file_data(config_file_data)

        if args.proxy:
            user_proxy = eval(args.proxy)
            if isinstance(user_proxy, list):
                self.proxy = args.proxy
            elif isinstance(user_proxy, str):
                self.proxy = str(user_proxy).split(';')
            else:
                print("Wrong proxy format specified.Exiting")
                sys.exit(0)

        if not self.subtitle_lang:
            self.subtitle_lang = utils.get_value_from_list(args.subtitle_language[0], supported_languages)
        if not self.subtitle_extension:
            self.subtitle_extension = utils.get_value_from_list(args.file_extension[0], supported_extensions)
        if not self.download_location:
            if args.download_directory:
                self.download_location = args.download_directory[0]
            else:
                while not self.download_location:
                    self.download_location = input("Enter Download Location : ")

        if not args.set_cookie and path_util.file_exists(cwd, cookie_file_name):
            cookie_file_data = utils.read_file_data(cwd, cookie_file_name)
        else:
            cookie_from_user = self.get_cookie_from_user()
            cookie_written = utils.create_file(cwd, cookie_file_name,
                                               cookie_from_user if not args.set_cookie else args.set_cookie[0])
            if cookie_written:
                cookie_file_data = cookie_from_user

        if not cookie_file_data:
            current_try = 1
            while not cookie_file_data and self.max_tries_for_cookie >= current_try:
                cookie_from_user = self.get_cookie_from_user()
                cookie_written = utils.create_file(cwd, cookie_file_name, cookie_from_user)
                if cookie_written:
                    cookie_file_data = cookie_from_user
                else:
                    current_try += 1

        # Everything is set, let's call the main boss
        Hulu(url, cookie_file_data, self.subtitle_lang, self.subtitle_extension, self.download_location, self.proxy)

    def set_config_file_data(self, config_file_data):
        # We'll map the data to variables in this method
        config_file_data = dict(config_file_data)
        self.max_tries_for_cookie = config_file_data.get('max_tries_for_cookie', 5)
        self.download_location = config_file_data.get('download_location', None)
        self.subtitle_lang = config_file_data.get('subtitle_lang', None)
        self.subtitle_extension = config_file_data.get('subtitle_extension', None)
        # We're saving ';' separated proxy values. So, get the object and split it.
        _proxies = config_file_data.get('proxy', None)
        if _proxies:
            self.proxy = str(_proxies).split(';')
        return None

    @staticmethod
    def get_config_file_data():
        config = {
            'max_tries_for_cookie': None,
            'download_location': None,
            'subtitle_lang': None,
            'subtitle_extension': None,
            'proxies': []
        }
        return config

    @staticmethod
    def ask_config_file_data(config):
        config = dict(config)
        for conf in config:
            if conf == "max_tries_for_cookie":
                config[conf] = input("Value For {0}: ".format(conf))
                config[conf] = 5 if not config[conf] else config[conf]
            elif conf == "download_location":
                config[conf] = input("Value For {0}: ".format(conf))
                config[conf] = os.getcwd() if not config[conf] else config[conf]
            elif conf == "subtitle_lang":
                config[conf] = input("Value For {0}: ".format(conf))
                config[conf] = 'en' if not config[conf] else config[conf]
            elif conf == "subtitle_extension":
                config[conf] = input("Value For {0}: ".format(conf))
                config[conf] = 'srt' if not config[conf] else config[conf]
            elif conf == "proxies":
                config[conf] = input("Value For {0} (Split multiple proxies by ';'): ".format(conf))
            else:
                config[conf] = input("Value For {0} : ".format(conf))
        return config

    @staticmethod
    def get_cookie_from_user():
        cookie = None
        while not cookie:
            cookie = input("Paste Hulu Cookie Value : ")
        return cookie

    @staticmethod
    def add_argparse():
        parser = argparse.ArgumentParser(
            description="HuluSubs_dl is a command line tool to download subtitles from Hulu.")
        parser.add_argument('--version', action='store_true', help='Shows version and exits.')
        parser.add_argument('-cookie', '--set-cookie', nargs=1, help='Saves Hulu Cookie.', default=None)
        parser.add_argument('-url', '--hulu-url', nargs=1, help='Provides URL of the hulu video.', default=None)
        parser.add_argument('-dd', '--download-directory', nargs=1,
                            help='Decides the download directory of the subtitle(s).', default=None)
        parser.add_argument('-ext', '--subtitle-extension', nargs=1,
                            help='Decides the file extension of the final file.', default='srt')
        parser.add_argument('-lang', '--subtitle-language', nargs=1, help='Decides the language of the subtitle file.',
                            default='en')
        parser.add_argument('-skip-conf', '--skip-config', action='store_true', help='Skips reading config file.')
        parser.add_argument('-proxy', '--proxy', nargs=1, help='Provides the Proxy to be used.', default=[])
        parser.add_argument('-config', '--make-config', action='store_true', help='Creates/Resets Config File & exits.')
        args = parser.parse_args()
        return args
