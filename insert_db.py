#!/usr/bin/python3

import os
import sqlite3
import mutagen
import sys
from mutagen.easyid3 import EasyID3
conn = sqlite3.connect('songs.db')
c = conn.cursor()
c.execute('drop table songs;')
conn.commit()
c.execute('create table songs (ID INTEGER PRIMARY KEY AUTOINCREMENT, filepath varchar(256),filename varchar(128) , title varchar(64) , artist varchar(64) , genre varchar(32), com varchar(64));')
conn.commit()
dir = sys.argv[1];
for root, dirs, files in os.walk(dir):
  for file in files:
    if file.endswith('.mp3'): 
      filename = root+'/'+file
      print(filename)
      info = mutagen.File(filename, easy=True)
      mood = info['mood'][0]
      artist = info['artist'][0]
      genre = info['genre'][0]
      title = info['title'][0]
      t = (artist,genre,title,mood,file,root) 
      sql = "insert into songs (artist,genre,title,com,filename,filepath) values (?,?,?,?,?,?)"
      c.execute(sql,t)  
conn.commit()
conn.close()


#create table songs (ID INTEGER PRIMARY KEY AUTOINCREMENT, filepath varchar(256),filename varchar(128) , title varchar(64) , artist varchar(64) , genre varchar(32), com varchar(64));

