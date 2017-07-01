#!/usr/bin/env python


import os
import glob

for item in glob.glob(os.path.join(".", "*.py")):
        print item
