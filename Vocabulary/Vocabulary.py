# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 11:48:05 2019

@author: PRINCE
"""

''' 1. Total number of words in james_joyce_ulysses File  '''

total_words=0


with open("C://Users//PRINCE//Desktop//Internship//Text_File//james_joyce_ulysses.txt","r",encoding="utf8") as file:
    read_file = file.read()
    words = read_file.split()
          #print(words)
    total_words += len(words)

print("Total_words",total_words)


''' 2. Total number of unique words in james_joyce_ulysses File  '''

total_unique_words=0


with open("C://Users//PRINCE//Desktop//Internship//Text_File//james_joyce_ulysses.txt","r",encoding="utf8") as file:
    read_file = file.read()
    words = read_file.split()
          #print(words)
    total_unique_words += len(set(words))

print("Total_words",total_unique_words)



''' 3. Unique words and total words in all Files ['sons_and_lovers_lawrence.txt','metamorphosis_kafka.txt','the_way_of_all_flash_butler.txt','robinson_crusoe_defoe.txt','to_the_lighthouse_woolf.txt','james_joyce_ulysses.txt','moby_dick_melville.txt']
'''


# Method For finding Unique Words
def file_unique_words(fname):
    total_unique_words=0
    with open(fname,"r",encoding="utf8") as file:
        read_file = file.read()
        words = read_file.split()
          #print(words)
        total_unique_words += len(set(words))
            
    return total_unique_words


print('unique_f1',file_unique_words("C://Users//PRINCE//Desktop//Internship//Text_File//james_joyce_ulysses.txt"))
print('unique_f2',file_unique_words("C://Users//PRINCE//Desktop//Internship//Text_File//metamorphosis_kafka.txt"))
print('unique_f3',file_unique_words("C://Users//PRINCE//Desktop//Internship//Text_File//moby_dick_melville.txt"))
print('unique_f4',file_unique_words("C://Users//PRINCE//Desktop//Internship//Text_File//robinson_crusoe_defoe.txt"))
print('unique_f5',file_unique_words("C://Users//PRINCE//Desktop//Internship//Text_File//sons_and_lovers_lawrence.txt"))
print('unique_f6',file_unique_words("C://Users//PRINCE//Desktop//Internship//Text_File//the_way_of_all_flash_butler.txt"))
print('unique_f7',file_unique_words("C://Users//PRINCE//Desktop//Internship//Text_File//to_the_lighthouse_woolf.txt"))



# Method For finding Total Words
def file_total_words(fname):
    total_words=0
    with open(fname,"r",encoding="utf8") as file:
        read_file = file.read()
            #print(type(line))
        words = read_file.split()
            #print(words)
        total_words += len(words)
            
    return total_words

print('Total_f1',file_total_words("C://Users//PRINCE//Desktop//Internship//Text_File//james_joyce_ulysses.txt"))
print('Total_f2',file_total_words("C://Users//PRINCE//Desktop//Internship//Text_File//metamorphosis_kafka.txt"))
print('Total_f3',file_total_words("C://Users//PRINCE//Desktop//Internship//Text_File//moby_dick_melville.txt"))
print('Total_f4',file_total_words("C://Users//PRINCE//Desktop//Internship//Text_File//robinson_crusoe_defoe.txt"))
print('Total_f5',file_total_words("C://Users//PRINCE//Desktop//Internship//Text_File//sons_and_lovers_lawrence.txt"))
print('Total_f6',file_total_words("C://Users//PRINCE//Desktop//Internship//Text_File//the_way_of_all_flash_butler.txt"))
print('Total_f7',file_total_words("C://Users//PRINCE//Desktop//Internship//Text_File//to_the_lighthouse_woolf.txt"))




''' 4. Special Words in Ulysses novel by comparing with others, words which are only used in Ulysses, store it in a file. '''

def file_unique_words2(fname):
    total_unique_words=0
    with open(fname,"r",encoding="utf8") as file:
        read_file = file.read()
        words = read_file.split()
          #print(words)
        total_unique_words = set(words)
            
    return total_unique_words


unique_f1=file_unique_words2("C://Users//PRINCE//Desktop//Internship//Text_File//james_joyce_ulysses.txt")
unique_f2=file_unique_words2("C://Users//PRINCE//Desktop//Internship//Text_File//metamorphosis_kafka.txt")
unique_f3=file_unique_words2("C://Users//PRINCE//Desktop//Internship//Text_File//moby_dick_melville.txt")
unique_f4=file_unique_words2("C://Users//PRINCE//Desktop//Internship//Text_File//robinson_crusoe_defoe.txt")
unique_f5=file_unique_words2("C://Users//PRINCE//Desktop//Internship//Text_File//sons_and_lovers_lawrence.txt")
unique_f6=file_unique_words2("C://Users//PRINCE//Desktop//Internship//Text_File//the_way_of_all_flash_butler.txt")
unique_f7=file_unique_words2("C://Users//PRINCE//Desktop//Internship//Text_File//to_the_lighthouse_woolf.txt")



len(unique_f1-unique_f2-unique_f3-unique_f4-unique_f5-unique_f6-unique_f7)

f = open("C://Users//PRINCE//Desktop//Internship//Text_File//Unique_ulysses.txt",'w')

f.write(str(set(unique_f1-unique_f2-unique_f3-unique_f4-unique_f5-unique_f6-unique_f7)))


''' 5. Common Words - Find the words which occur in every book.'''

sets = [unique_f1,unique_f2,unique_f3,unique_f4,unique_f5,unique_f6,unique_f7]

common = set.intersection(*sets)

len(common)

