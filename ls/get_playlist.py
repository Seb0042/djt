#!/usr/bin/python3
import owncloud
import sys
import os
from shutil import copyfile

f = sys.argv[1].replace('oc://','')
fd = sys.argv[2]
#fd = os.path.basename(f)
oc = owncloud.Client('https://www.djtabasco.dance/nextcloud')
oc.login('djt', 'JQ2Do-fBf27-ejS7b-BZ2C9-iryTN')
oc.get_file(f, fd)
fread = open(fd, "r")
text = fread.read()
print(text)
fread.close()
#os.remove(fd)
