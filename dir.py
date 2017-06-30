#!/usr/bin/env python

import os

# "." to search in current directory "/" to search in root
for item in os.listdir("."):
    if os.path.isfile(item):
        print item + " is a file"

    elif os.path.isdir(item):
        print item + " is a directiory"

    else: 
        print "unknown!"
