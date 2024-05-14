#!/usr/bin/env python
import sys
from sys import argv

transcript_handle=open("%s"%argv[1])
out_handle=open("%s_PANTHER.txt"%argv[1],"w")
panther_handle=open("bird-brain-proteins_pantherScore.out","r")
pantherDict={}

for line in panther_handle:
	transcript=line.split()[0].split(".p")[0]
	pantherDict[transcript]=line
x=0
y=0
written=[]
for line in transcript_handle:
	x+=1
	t=line.rstrip("\n")	
	if t in pantherDict.keys():
		if t in written:
			print("redundant: %s"%t)	
		else:
			y+=1
			out_handle.write("%s"%pantherDict[t])
			written.append(t)
print("of %s transcripts found %s matches in PANTHER."%(x,y))
out_handle.close()
transcript_handle.close()
panther_handle.close()
