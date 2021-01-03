#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
from hulu_subs_dl import HuluSubsDl

if __name__ == "__main__":
    HuluSubsDl(sys.argv[1:], os.getcwd())
    sys.exit()
