#!/usr/bin/env python
import sys
from sys import argv

stringtie_handle=open("stringtie_merged.gtf","r")
transcript_handle=open("%s"%argv[1])
out_handle=open("%s_KnownGenes.txt"%argv[1],"w")
geneDict={}
x=0
for line in stringtie_handle:
	gene='null'
	transcript='null'
	if line[0:1]!='#':
		x+=1
		if line.split('\t')[2]=="transcript":
			items=line.split('\t')[8]
			for i in items.split(';'):
				if 'gene_name' in i:
					gene=i.split('"')[1]
					#print(gene)
				if 'transcript_id' in i:
					transcript=i.split('"')[1]
			#print("gene %s transcript %s"%(gene,transcript))
			#print(geneDict)
			if transcript != 'null' and gene !='null':
				geneDict[transcript]=gene
		if x%10000==0:
			print("processed %s thousand entries"%(x/1000))
#print(geneDict)
found=[]
for line in transcript_handle:
	t=line.rstrip("\n")	
	if t in geneDict.keys():
		if not (geneDict[t] in found):
			out_handle.write('%s\n'%geneDict[t])
			found.append(geneDict[t])
		

out_handle.close()
stringtie_handle.close()
transcript_handle.close()
