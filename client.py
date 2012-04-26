# -*- coding: utf-8 -*-
import socket
import os, os.path
import sys
import re
import time

#------------------------------------------------------------------------
# Put here path to debug log that is currently written by skypekit runtime
# you need run "skypekit -d logname" before edit this
# also you can parse log by youself like "tail -F /some/folder/logname | grep -a noticing" and use client.py only for send username into socket
PathToLog = "/some/folder/logname"


if len(sys.argv) == 1:
        print('Usage: python skyip.py <skypename>')
        sys.exit();

Username = sys.argv[1]

if os.path.exists( "/tmp/skype_iplookup" ):
	client = socket.socket( socket.AF_UNIX, socket.SOCK_DGRAM )
	client.connect( "/tmp/skype_iplookup" )
	client.send(Username)
	client.close()
	time.sleep(3)
	File = open(PathToLog,'rb').readlines()
	finds = []
	for matches in File:
		finded = re.findall('.*noticing.{0}.0.*-r(.*?)-l(.*?:[0-9]*?)[^0-9].*'.format(Username), matches)
		if len(finded)>0:
			finds.append('%s - %s'%(finded[0][0],finded[0][1]))
	finds = list(set(finds))
	for f in finds:
		print f
else:
  print "Can't connect to unix socket /tmp/skype_iplookup"
