#!/usr/bin/python3

import xspf

x = xspf.Xspf()
x.title = "LetsDance Salsa playlist"
x.info = "http://listen.shoutcast.com/letsdance"

tr1 = xspf.Track()
tr1.title = "Yo"
tr1.creator = "Not Me"
tr1.location = "oc://Salsa/Not Me/Yo"
x.add_track(tr1)

print( x.toXml() )
