#!/usr/bin/python3

import os
import errno
import mutagen
from mutagen.easyid3 import EasyID3
dir = '/data/Music'
for root, dirs, files in os.walk(dir):
  for file in files:
    if file.endswith('.mp3'):
      filename = root+'/'+file
      info = mutagen.File(filename, easy=True)
      #print(info['artist'][0])
      #print(info['title'][0])
      dir=info['genre'][0].replace('/','')
      print(dir)
      try:
        os.mkdir(dir)
      except OSError as exc:
        if exc.errno != errno.EEXIST:
          raise
        pass

#dict_keys(['musicbrainz_albumid', 'tracknumber', 'album', 'conductor', 'compilation', 'musicbrainz_albumartistid', 'musicbrainz_trmid', 'musicbrainz_discid', 'barcode', 'performer', 'albumsort', 'length', 'artist', 'acoustid_id', 'title', 'discnumber', 'copyright', 'albumartistsort', 'musicbrainz_workid', 'website', 'musicbrainz_albumstatus', 'media', 'version', 'composersort', 'replaygain_*_gain', 'titlesort', 'composer', 'date', 'arranger', 'author', 'originaldate', 'lyricist', 'musicbrainz_albumtype', 'language', 'performer:*', 'organization', 'artistsort', 'acoustid_fingerprint', 'musicip_puid', 'genre', 'replaygain_*_peak', 'musicbrainz_artistid', 'catalognumber', 'mood', 'asin', 'discsubtitle', 'releasecountry', 'musicbrainz_releasetrackid', 'encodedby', 'bpm', 'isrc', 'musicbrainz_releasegroupid', 'musicip_fingerprint', 'musicbrainz_trackid'])

