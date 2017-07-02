#!/usr/bin/env python
  
import subprocess

print'''

PRINTING SUBPROCESS\n'''

writer = open('sub.txt', 'w')


line = subprocess.check_output(['ls', '-al'])

lol = str(line)
writer.write(lol)
writer.close()
