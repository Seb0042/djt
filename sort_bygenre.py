#!/usr/bin/python3

import os
import sys
import errno
import mutagen
from shutil import copyfile, move
from pathlib import Path
from mutagen.easyid3 import EasyID3


dir = sys.argv[1]

def mdir(dname):
  try:
    os.mkdir(dname)
  except OSError as exc:
    if exc.errno != errno.EEXIST:
      raise
    pass

def getdgenre(artist,dname):
  artist = artist.replace('/','')
  p = dname.replace(artist,'')
  return os.path.basename(os.path.normpath(p))


def movefile(src,dst,genre,artist,file):
  artist = artist.replace('/','')
  dgpath = dst+'/'+genre
  dpath = dgpath+'/'+artist
  dfile = dpath+'/'+file
  mdir(dgpath)
  mdir(dpath)
  my_file = Path(dfile)
  if my_file.exists():
    print("ERROR: File "+dfile+" already exists (from:"+src+")")
  else:
    print("moving "+src+" to "+dfile)
    move(src,dfile)
  
for root, dirs, files in os.walk(dir):
  for file in files:
    if file.endswith('.mp3') or file.endswith('.mpg') or file.endswith('.m4a'):
      filename = root+'/'+file
      info = mutagen.File(filename, easy=True)
      dgenre = getdgenre(info['artist'][0],root)
      tgenre = info['genre'][0].replace('/','')
      if ( tgenre != dgenre ):
        movefile(filename,dir,tgenre,info['artist'][0],file)
 
