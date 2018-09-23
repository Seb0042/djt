#!/usr/bin/python3

import os
import sqlite3
import mutagen
impot sys

from mutagen.easyid3 import EasyID3
conn = sqlite3.connect('songs.db')
c = conn.cursor()
dir = sys.argv[1]
for root, dirs, files in os.walk(dir):
  for file in files:
    if file.endswith('.mp3'):
      filename = root+'/'+file
      info = mutagen.File(filename, easy=True)
      for tag in ['artist', 'genre', 'title', 'comment']:
        if tag not in info.keys():
          if tag == 'artist':
            info['artist'] = 'Unknown'
          elif tag == 'title':
            info['title'] = 'Unknown'
          elif tag == 'genre':
            info['genre'] = 'Unknown'
          elif tab == 'comment':
            info['comment'] = 'None'
      info.save()
conn.commit()
conn.close()



#dict_keys(['musicbrainz_albumid', 'tracknumber', 'album', 'conductor', 'compilation', 'musicbrainz_albumartistid', 'musicbrainz_trmid', 'musicbrainz_discid', 'barcode', 'performer', 'albumsort', 'length', 'artist', 'acoustid_id', 'title', 'discnumber', 'copyright', 'albumartistsort', 'musicbrainz_workid', 'website', 'musicbrainz_albumstatus', 'media', 'version', 'composersort', 'replaygain_*_gain', 'titlesort', 'composer', 'date', 'arranger', 'author', 'originaldate', 'lyricist', 'musicbrainz_albumtype', 'language', 'performer:*', 'organization', 'artistsort', 'acoustid_fingerprint', 'musicip_puid', 'genre', 'replaygain_*_peak', 'musicbrainz_artistid', 'catalognumber', 'mood', 'asin', 'discsubtitle', 'releasecountry', 'musicbrainz_releasetrackid', 'encodedby', 'bpm', 'isrc', 'musicbrainz_releasegroupid', 'musicip_fingerprint', 'musicbrainz_trackid'])

