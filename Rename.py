#!/usr/bin/env python
import sys
from sys import argv

panther_handle=open("%s"%argv[1],"r")
out_handle=open("%s_RENAMED.txt"%argv[1],"w")
x=0
y=0
written=[]
for line in panther_handle:
	x+=1
	name=line.split()[0]
	numitems=len(line.split())
	if numitems<20:
		rest='\t'.join(line.split()[1:])
	else:
		rest='\t'.join(line.split()[1:18])
	if name in written:
		print("redundant: %s"%name)
	else:
		y+=1
		out_handle.write("%s\t%s\n"%(x,rest))
		written.append(name)
print("of %s, renamed %s lines"%(x,y))
out_handle.close()
panther_handle.close()
