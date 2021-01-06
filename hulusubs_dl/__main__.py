#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.append("..")
from hulusubs_dl.__version__ import __version__
from hulusubs_dl.cust_utils import *
from hulusubs_dl.hulu_subs_dl import HuluSubsDl

if __name__ == "__main__":
    HuluSubsDl(sys.argv[1:], os.getcwd())
    sys.exit()
