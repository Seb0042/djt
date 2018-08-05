#! /bin/bash

d=sum
export IFS="|"

cat liste | while read nom p
do
	find /data/Music -name "$nom" -exec md5sum {} \; | while read l
	do
		ck=$(echo $l | cut -f1 -d' ')
		echo "$ck $p " >> ${d}/${nom}
	done
done
