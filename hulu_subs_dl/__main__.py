#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from hulu_subs_dl import HuluSubsDl
import __version__
import cust_utils
import api

if __name__ == "__main__":
    HuluSubsDl(sys.argv[1:], os.getcwd())
    sys.exit()
