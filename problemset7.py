#!/usr/bin/env python3

import re
#read the text to start
nobody_text = open("Python_07_nobody.txt", "r")
nobody_read = nobody_text.read()
print(nobody_read)

#find nobody in text
find =  re.findall(r"Nobody", nobody_read)  
print(find)

#find in another way
if re.findall(r"Nobody", nobody_read):
  print('Found a bunch of Nobody')

#prints a list of 'Nobody"
nobody_events = re.findall(r"Nobody", nobody_read)
print(nobody_events)

#print each Nobody
for nobody in re.findall(r"Nobody", nobody_read):
  print(nobody)

with open("Python_07_nobody.txt", "r") as text:
  string = text.read()
  print(string)
  print(type(string))
  for location in re.finditer(r"Nobody", string):
    whole = location.group()
    start_end = location.span()
    print(whole, start_end)

#In the file Python_07_nobody.txt substitute every occurrence of 'Nobody' with your favorite name and write an output file with that person's name (ex. Michael.txt).
with open("Python_07_nobody.txt", "r") as text_read, open("Michael.txt", "w") as text_write:
  for line in text_read:
    line = re.sub(r"Nobody", 'Michael', string)
    print(line)
    text_write.write(str(line))
print("wrote 'Michael.txt'")
 
 #text_write.write(new_string = re.sub(r"Nobody", 'Michael', string))

#print(type(nobody_text))
#find the position of Nobody
#pattern = 'Nobody'
#match = (re.search(pattern,nobody_read))

#location = [match.span(span) for span in nobody]
#print(location)

#returns match object
#print(match)

#returns the spanning (start and end indexes)
#print(match.span())

#Python_07.fasta
print(type('Python_07.fasta'))
fasta_dict = {}
with open("Python_07.fasta", "r") as fasta:
  for line in fasta:
    if line.startswith('>'):
      header = line
      fasta_dict[header] = ''
    else:
      seq = line
      fasta_dict[header] += seq
print(fasta_dict)
   # re.sub(''
   # key =  


 #for line in fasta:
   # line = line.
     # print(fasta) #goal is to print locus tag
   # else:
     # print('nada')
