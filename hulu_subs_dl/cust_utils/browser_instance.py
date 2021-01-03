#!/usr/bin/env python
# -*- coding: utf-8 -*-
import requests
import json


def get_request(url, cookie_value, text_only=False, **kwargs):
    if not cookie_value:
        raise Warning("No Cookie Value Provided. Exiting")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate',
        'Cookie': cookie_value
    }

    sess = requests.session()
    connection = sess.get(url, headers=headers)

    if connection.status_code != 200:
        print("Whoops! Seems like I can't connect to website.")
        print("It's showing : %s" % connection)
        print("Run this script with the --verbose argument and report the issue along with log file on Github.")
        print("Can't connect to website %s" % url)
        return None
    else:
        if text_only:
            return connection.content
        return json.loads(connection.text.encode("utf-8"))


def post_request(url, data, cookie_value, **kwargs):
    if not cookie_value:
        raise Warning("No Cookie Value Provided. Exiting")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept': '*/*',
        'Content-Type': 'application/json',
        'Cookie': cookie_value
    }

    sess = requests.session()
    connection = sess.post(url, data=data, headers=headers)

    if connection.status_code != 200:
        print("Whoops! Seems like I can't connect to website.")
        print("It's showing : %s" % connection)
        print("Run this script with the --verbose argument and report the issue along with log file on Github.")
        print("Can't connect to website %s" % url)
        return None
    else:
        return json.loads(connection.text.encode("utf-8"))
