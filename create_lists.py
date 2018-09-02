#!/usr/bin/python3

import os
import sqlite3
import sys
from mutagen.easyid3 import EasyID3
conn = sqlite3.connect('songs.db')
c = conn.cursor()
sql_genre = 'select distinct genre from songs order by genre;'
for row in c.execute(sql_genre):
  genre = row[0]
  t = (row[0],)
  
  cg = conn.cursor()
  radio_file = open('Target/'+genre.replace('/','')+'/'+'radio.txt', 'w')
  sql_radio = "select filepath,filename from songs where genre = ? and ( com = 'Mix' or com = 'Listen' or com = 'Radio' )"
  for row_radio in cg.execute(sql_radio,t):
    radio_file.write(row_radio[0].replace('Target/'+genre+'/','')+'/'+row_radio[1]+'\n')
  cg.close()
  radio_file.close()

  
  cg = conn.cursor()
  listen_file = open('Target/'+genre.replace('/','')+'/'+'listen.txt', 'w')
  sql_listen = "select filepath,filename from songs where genre = ? and ( com = 'Mix' or com = 'Listen' )"
  for row_listen in cg.execute(sql_listen,t):
    listen_file.write(row_listen[0].replace('Target/'+genre+'/','')+'/'+row_listen[1]+'\n')
  cg.close()
  listen_file.close()

  cg = conn.cursor()
  mix_file = open('Target/'+genre.replace('/','')+'/'+'mix.txt', 'w')
  sql_mix = "select filepath,filename from songs where genre = ? and com = 'Mix'"
  for row_mix in cg.execute(sql_mix,t):
    mix_file.write(row_mix[0].replace('Target/'+genre+'/','')+'/'+row_mix[1]+'\n')
  cg.close()
  mix_file.close()

c.close()
conn.close()


#create table songs (ID INTEGER PRIMARY KEY AUTOINCREMENT, filepath varchar(256),filename varchar(128) , title varchar(64) , artist varchar(64) , genre varchar(32), com varchar(64));

