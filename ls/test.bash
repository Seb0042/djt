#!/home/djt/.opam/4.05.0/bin/liquidsoap



def oc_protocol(~rlog,~maxtime,arg) =
  extname = file.extension(dir_sep="/",arg)
  [process_uri(extname=extname,"get_oc_file.py oc:#{arg} $(output)")]
end
add_protocol("oc",oc_protocol,doc="Fetch files from OC using custom python", syntax="oc://genre/file")

