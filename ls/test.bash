#!/home/djt/.opam/4.05.0/bin/liquidsoap

set("log.stdout", true)
set("log.file.path","logs/launch.log")
set("log.file",true)
set("log.level",3)

def oc_protocol(~rlog,~maxtime,fic) =
  extname = file.extension(dir_sep="/",fic)
  [process_uri(extname=extname,"./get_oc_file.py oc:#{fic} $(output)")]
end
add_protocol("oc",oc_protocol,doc="Fetch files from OC using custom python", syntax="oc://fic")

default = single("default/single.mp3")
Salsa = playlist("oc://Salsa/radio.txt")
day     = Salsa
night   = Salsa


radio = fallback([ request.queue(id="request"),
                    switch([({ 6h-22h }, day),
                            ({ 22h-6h }, night)]),
                    default])


output.alsa(radio)

