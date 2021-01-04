#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from pathlib import Path


def get_abs_path_name(file_path, file_name):
    return os.path.abspath(file_path + file_name)


def file_exists(file_path, file_name):
    return os.path.isfile(get_abs_path_name(file_path, file_name))


def create_paths(directory):
    Path(os.path.abspath(directory)).mkdir(parents=True, exist_ok=True)
    return os.path.abspath(directory)
