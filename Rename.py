#!/usr/bin/env python
import sys
from sys import argv

panther_handle=open("%s"%argv[1],"r")
out_handle=open("%s_RENAMED.txt"%argv[1],"w")
x=0
for line in panther_handle:
	x+=1
	rest=[]
	rest='\t'.join(line.split()[1:])
	out_handle.write("%s\t%s\n"%(x,rest))
print("renamed %s lines"%x)
out_handle.close()
panther_handle.close()
