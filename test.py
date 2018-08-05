#!/usr/bin/python3

import os
import sys
from mutagen.easyid3 import EasyID3
from mutagen.mp3 import MP3

audio = EasyID3(sys.argv[1])
for tag in audio.keys():
  print(tag)
audio['genre'] = 'Unknown'
audio.save()
