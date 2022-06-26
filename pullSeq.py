#!/usr/bin/env python3
#Created: 2022 January 22
#Updated: 2022 June 26
#Modified by: Ariane Thomas

from Bio import SeqIO
import sys
			
def pullandaddseqbylist(fileofseqs, filelist, finishedfile):
	'''pulls sequences from a file using a list and then adds them to the finished file'''
	list = []
	
	#creates list from file
	with open(filelist, "r") as file:
		for line in file.readlines():
			linewithoutcarrot = line.strip(">\n")
			list.append(linewithoutcarrot)
		
		final_list = []

		for seq_record in SeqIO.parse(fileofseqs, "fasta"):
			if seq_record.id in list:
				#may need to be seq_record.description
				final_list.append(seq_record)

		SeqIO.write(final_list, finishedfile, "fasta")
	
		
pullandaddseqbylist(sys.argv[1], sys.argv[2], sys.argv[3])

