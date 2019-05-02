# -*- coding: utf-8 -*-
"""
Created on Thu May  2 17:23:12 2019

@author: PRINCE
"""

# For romeo.txt file
dict_1 ={}
with open("romeo.txt",'r',encoding="utf8") as file_1:
    data_1 = file_1.read()
    print("List of words in file:\n",data_1.split())
    for word in data_1.split():
        if word not in dict_1:
            dict_1[word] = 1
        else:
            dict_1[word] += 1 
            
print("\nWords and thier count in dictonary:\n",dict_1)


        
        
# For romeo2.txt file
        
import re

dict_2 = {}
with open("romeo2.txt",'r',encoding="utf8") as file_2:
    data_2 = re.sub(r"[^a-zA-Z0-9\s]",'',file_2.read())
    print("List of words without special character in file:\n",data_2.split())
    for word in data_2.split():
        if word not in dict_2:
            dict_2[word] = 1
        else:
            dict_2[word] += 1 
            
print("\nWords and thier count in dictonary:\n",dict_2)
