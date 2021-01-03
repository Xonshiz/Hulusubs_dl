#!/usr/bin/env python
# -*- coding: utf-8 -*-
from . import path_util
DEFAULT_SUB_EXT = ['vtt', 'ttml', 'smi']


def get_value_from_list(value, list_object):
    if type(list_object) == type(list):
        for x in list_object:
            if str(x).lower().strip() == str(value).lower().strip():
                return x
        return list_object[0]


def get_playlist_body(eab_id):
    body = {
        "deejay_device_id": 190,
        "version": 1,
        "all_cdn": True,
        "content_eab_id": eab_id,
        "region": "US",
        "xlink_support": False,
        "limit_ad_tracking": False,
        "ignore_kids_block": False,
        "language": "en",
        "unencrypted": True,
        "interface_version": "1.9.0",
        "network_mode": "wifi",
        "play_intent": "resume",
        "playback": {
            "version": 2,
            "video": {
                "codecs": {
                    "values": [
                        {
                            "type": "H264",
                            "width": 1024,
                            "height": 546,
                            "framerate": 60,
                            "level": "4.2",
                            "profile": "HIGH"
                        }
                    ],
                    "selection_mode": "ONE"
                }
            },
            "audio": {
                "codecs": {
                    "values": [
                        {
                            "type": "AAC"
                        }
                    ],
                    "selection_mode": "ALL"
                }
            },
            "drm": {
                "values": [
                    {
                        "type": "WIDEVINE",
                        "version": "MODULAR",
                        "security_level": "L3"
                    },
                    {
                        "type": "PLAYREADY",
                        "version": "V2",
                        "security_level": "SL2000"
                    }
                ],
                "selection_mode": "ALL",
                "hdcp": False
            },
            "manifest": {
                "type": "DASH",
                "https": True,
                "multiple_cdns": True,
                "patch_updates": True,
                "hulu_types": True,
                "live_dai": True,
                "secondary_audio": True,
                "live_fragment_delay": 3
            },
            "segments": {
                "values": [
                    {
                        "type": "FMP4",
                        "encryption": {
                            "mode": "CENC",
                            "type": "CENC"
                        },
                        "https": True
                    }
                ],
                "selection_mode": "ONE"
            }
        }
    }
    return body


def get_eab_id_formatted(eab_id):
    eab_id = str(eab_id).replace('%3A', ':')
    eab_ids = eab_id.split('::')
    eab_formatted = 'EAB::{0}::{1}::{2}'.format(eab_ids[0], "NULL" if len(eab_ids) < 3 else eab_ids[1],
                                                "NULL" if len(eab_ids) < 3 else eab_ids[-1])
    # temp_eab = None
    # if "EAB" not in eab_id:
    #     temp_eab = "EAB::" + eab_id
    # temp_eab = str(temp_eab).replace(':', '%3A').strip()
    return eab_formatted.replace(':', '%3A').strip()


def get_language_code(language):
    return 'en'


def get_language_from_code(language_code):
    return 'English'


def create_file(file_path, file_name, data_to_write):
    if not isinstance(data_to_write, str):
        data_to_write = str(data_to_write)
    if not data_to_write or not str(data_to_write).strip():
        print("Empty Data Provided For {0}".format(file_name))
        return False
    file_location = path_util.get_abs_path_name(file_path, file_name)
    with open(file_location, 'w') as f:
        f.write(data_to_write)
        f.flush()
    return True


def create_file_binary_mode(file_path, file_name, data_to_write):
    if not data_to_write or not str(data_to_write).strip():
        print("Empty Data Provided For {0}".format(file_name))
        return False
    file_location = path_util.get_abs_path_name(file_path, file_name)
    with open(file_location, 'wb') as f:
        f.write(data_to_write)
        f.flush()
    return True


def read_file_data(file_path, file_name):
    file_location = path_util.get_abs_path_name(file_path, file_name)
    content = None
    with open(file_location, 'r') as f:
        content = f.read().strip()
    return None if content == "" else content