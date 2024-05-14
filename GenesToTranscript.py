#!/usr/bin/env python
import sys
from sys import argv

stringtie_handle=open("stringtie_merged.gtf","r")
module_handle=open("%s"%argv[1])
out_handle=open("%s_transcripts.txt"%argv[1],"w")
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
				if 'gene_id' in i:
					gene=i.split('"')[1]
				if 'transcript_id' in i:
					transcript=i.split('"')[1]
					break
			#print("gene %s transcript %s"%(gene,transcript))
			#print(geneDict)
			if gene in geneDict.keys():			
				current=geneDict[gene]
				current.append(transcript)
				geneDict[gene]=current
			else:
				newlist=[]
				newlist.append(transcript)
				geneDict[gene]=newlist
		if x%10000==0:
			print("processed %s thousand entries"%(x/1000))

for line in module_handle:
	g=line.split(',')[0]	
	if '|' in g:
		g1=g.split('|')[0]
		g2=g.split('|')[1]
		if g1!=g2:
			if g1 in geneDict.keys():
				transcriptlist=geneDict[g1]
				for t in transcriptlist:
					out_handle.write('%s\n'%t)
			if g2 in geneDict.keys():
				transcriptlist=geneDict[g2]
				for t in transcriptlist:
					out_handle.write('%s\n'%t)
		else:
			if g1 in geneDict.keys():
				transcriptlist=geneDict[g1]
				for t in transcriptlist:
					out_handle.write('%s\n'%t)
	else:
		if g in geneDict.keys():
			transcriptlist=geneDict[g]
			for t in transcriptlist:
				out_handle.write('%s\n'%t)
		

out_handle.close()
stringtie_handle.close()
module_handle.close()
