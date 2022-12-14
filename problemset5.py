#!/usr/bin/env python3

#create a dictionary of your favorite things
fav_dict = {'book':'don quijote','song':'billie holiday - any old time','tree':'birch'}

#print your favorite book
print(fav_dict['book'])

#print your favorite book but use a variable in the key
fav_thing = 'book'
print(fav_dict[fav_thing])

#add your favorite organism to the dictionary
fav_dict['organism'] = 'shark'
print(fav_dict) #{'book': 'don quijote', 'song': 'billie holiday - any old time', 'tree': 'birch', 'organism': 'shark'}
fav_thing = 'organism'
print(fav_dict[fav_thing]) #shark

#Take a value from the command line for fav_thing and print the value of that item from the dictionary. Maybe you want to print out all the keys to the user so that they know what to pick from. Check out input(). Here is a link.

for fav in fav_dict:
  value = fav_dict[fav]
  print(value)

#favs=input()
#print('your key is', favs)
#this prints organism

#change the value of your favorite organism
fav_dict['organism'] = 'Xanthomonas'
print('your dictionary currently is:', fav_dict)
print('your organism currently is:', fav_dict[fav_thing])

#Make a set using the two different syntaxes for creating a set myset = set() and myset2 = {}. What is the difference? Does it matter how you make it?

mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

print(mySet)
print(mySet2)
#{'G', 'A', 'T'}
#{'ATGCCT'}

#Write a script to find the intersection, difference, union, and symetrical difference between these two sets.
#Set A = 3 14 15 9 26 5 35 9
#Set B = 60 22 14 0 9

mySetA = set('3, 14, 15, 9, 26, 5, 35, 9')
mySetB = set('60, 22, 14, 0, 9')

#union
print(mySetA | mySetB)
#intersection
print(mySetA & mySetB)
#difference
print(mySetA -  mySetB)
#symmetric differce
print(mySetA ^ mySetB)

#If you create a set using a DNA sequence, what will you get back? Try it with this sequence:

dna = set('GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC')

print(dna)

#{'T', 'G', 'C', 'A'}

nt_count = {}

dna_seq = 'GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'

dna_seq_set = set(dna_seq)
print('unique nt:', dna_seq_set) #unique nt: {'G', 'T', 'C', 'A'}

#iterate through each unique nucleotide
for nt in dna_seq:
  if nt in nt_count:
    nt_count[nt] += 1 #this runs through the set you created
  else:
    nt_count[nt] = 1
#count the number of this unique nt in dna
  #nt_count[nt] += 1 #this runs through the set you created
 # nt_count[nt] = count 

print('nt count:', nt_count) #{'G': 206, 'A': 360, 'C': 227, 'T': 370}
print('the GC content is:', nt_count['G']/nt_count['C'])

