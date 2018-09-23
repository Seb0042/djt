#!/usr/bin/python3
import owncloud
import sys
import os

f = sys.argv[1].replace('ocfl://','')
rd = sys.argv[2]
fd = os.path.basename(f)
print(fd)
print(rd)
oc = owncloud.Client('https://www.djtabasco.dance/nextcloud')
oc.login('djt', 'JQ2Do-fBf27-ejS7b-BZ2C9-iryTN')
oc.get_file(f, fd)
exit(0)
