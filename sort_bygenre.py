#!/usr/bin/python3

import os
import sys
import errno
import mutagen
from shutil import copyfile

from mutagen.easyid3 import EasyID3


dir = sys.argv[1]

def cdir(dname):
  try:
    os.mkdir(dir+'/'+dname)
  except OSError as exc:
    if exc.errno != errno.EEXIST:
      raise
    pass

def getdgenre(artist,dname):
  p = dname.replace(artist,'')
  return os.path.basename(os.path.normpath(p))
  
for root, dirs, files in os.walk(dir):
  for file in files:
    if file.endswith('.mp3') or file.endswith('.mpg') or file.endswith('.m4a'):
      filename = root+'/'+file
      info = mutagen.File(filename, easy=True)
      dgenre = getdgenre(info['artist'][0],root)
      if ( info['genre'][0] != dgenre ):
        print(filename+"##"+genre+"##"+dgenre)
