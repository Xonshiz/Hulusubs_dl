#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from hulusubs_dl import __version__
from hulusubs_dl import cust_utils
from hulusubs_dl import hulu_subs_dl

if __name__ == "__main__":
    hulu_subs_dl.HuluSubsDl(sys.argv[1:], os.getcwd())
    sys.exit()
