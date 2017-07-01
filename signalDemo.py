#!/usr/bin/env python

import signal, sys

def SigAlarmHandler(signal, frame):
    print "Received alarm .... Shutting down .."
    sys.exit(0)

signal.signal(signal.SIGALRM, SigAlarmHandler)
signal.alarm(100)

print "Starting work ... waiting for alarm to quit :D "

while True:
    pass
