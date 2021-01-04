#!/usr/bin/env python
# -*- coding: utf-8 -*-

from . import cust_utils
import json

BASE_URL = 'https://discover.hulu.com/content/v3/entity'


def get_playlist_information(payload, cookie_value):
    if isinstance(payload, dict):
        payload = json.dumps(payload)
    response = cust_utils.browser_instance.post_request(url='https://play.hulu.com/v6/playlist', data=payload,
                                                        cookie_value=cookie_value)
    return response


def get_eab_id_metadata(eab_id, cookie_value, subtitle_lang='en'):
    url = BASE_URL + '?device_context_id=1&eab_ids={0}&language={1}&referral_host=www.hulu.com&schema=4'.format(
        str(eab_id).replace(':', '%3A'), subtitle_lang)
    response = cust_utils.browser_instance.get_request(url=url, cookie_value=cookie_value)
    return response


def get_full_eab_id(eab_id, cookie_value):
    url = 'https://discover.hulu.com/content/v5/deeplink/playback?namespace=entity&id={0}&schema=1&device_info=web:3.10.0&referralHost=production'.format(
        eab_id)
    response = cust_utils.browser_instance.get_request(url=url, cookie_value=cookie_value)
    return response


def get_series_metadata(series_eab_id, cookie_value):
    url = 'https://discover.hulu.com/content/v5/hubs/series/{0}?schema=1&limit=999&device_info=web:3.10.0&referralHost=production'.format(
        series_eab_id)
    response = cust_utils.browser_instance.get_request(url=url, cookie_value=cookie_value)
    return response


def get_series_season_metadata(series_eab_id, cookie_value, season):
    url = 'https://discover.hulu.com/content/v5/hubs/series/{0}/season/{1}?limit=999&schema=1&offset=0&device_info=web:3.10.0&referralHost=production'.format(
        series_eab_id, season)
    response = cust_utils.browser_instance.get_request(url=url, cookie_value=cookie_value)
    return response
