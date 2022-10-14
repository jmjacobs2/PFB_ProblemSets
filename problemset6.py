#!/usr/bin/env python3

seq_file_obj = open("Python_06.txt","r")
contents = seq_file_obj.read()
print(contents)

#uppercase each line
contents = contents.upper()
print(contents)

#for line in cont:
  #line.upper()
  #print(seq_file_obj)

#print each line to STDOUT

import sys

sys.stdout.write(contents) #prints out the same thing

#make a new txt called Python_0_uc.txt
with open("Python_06.txt","r") as seq_read, open("Python_06_uc.txt","w") as seq_write:
  print("wrote 'Python_06_uc.txt'")

#open a fastq file and report the number of lines, characters and average length of line

fastq = open("Python_06.fastq", "r")
contents = fastq.read()
#print(contents) removed because super big
with open("Python_06.fastq", "r") as fastq:
  for count, line in enumerate(fastq):
    pass
  characters = len(contents)
print('Total line in fastq', count + 1, 'and characters', characters)
fastq.close()

#write my first FASTA parser 
fasta_dict = {}
with open("Python_06.fasta", "r") as fasta:
  for line in fasta:
    line = line.rstrip()
    if line.startswith('>'):
      header = line
      fasta_dict[header] = ''
    else:
      seq = line
      fasta_dict[header] += seq
print(fasta_dict)

#with open("Python_06.fasta","r") as seq_read: # open("Python_06_fasta_parse.txt","w") as seq_write:

 # for line in fasta:
	
  #  line = line.rstrip() #removes lines
   # line = line.split()
   # print(line)
    #for count, line in enumerate(fasta):
 #       pass
#print(count + 1)  
   # line = line.lstrip('>')
   # gene_id,seq = line.split() #splits white space
   # fasta_parser[gene_id] = seq
   #print(line)

