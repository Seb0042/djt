#!/home/djt/.opam/4.05.0/bin/liquidsoap

set("log.stdout", true)
set("log.file.path","logs/launch.log")
set("log.file",true)
set("log.level",3)
set("server.telnet",true)

def nextcloud(~rlog,~maxtime,arg) =
  extname = file.extension(dir_sep="/",arg)
  [process_uri(extname=extname,"/data/djt/ls/get_file.bash '#{arg}' $(output)")]
end
add_protocol("nc",nextcloud,doc="Fetch files from nextcloud", syntax="nc://uri")

default = single("default/single.mp3")
Salsa = playlist(timeout=30.0,"nc://Salsa/radio.txt")
#Salsa = playlist("radio.txt")
day     = Salsa
night   = Salsa


radio = fallback([ request.queue(id="request"),
                    switch([({ 6h-22h }, day),
                            ({ 22h-6h }, night)]),
                    default])


output.alsa(radio)

