"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""

import re

lis=[]
for i in range(0,4):
    lis.append(input("Enter Number: "))


pattern = '[-+]?\d*\.+\d+'

for i in lis:
    result = re.match(pattern,i)
    if result:
        print('True')
    else:
        print('False')



"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

list1=[]
list2=[]

pattern = '^([a-zA-Z0-9_\-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]){2,4}$'


for i in range(0,3):
    list1.append(input('Email Address: '))
    
for i in list1:
    result = re.match(pattern,i)
    if result:
        list2.append(i)
        print('True')
    else:
        print('False')
        
list2.sort()
print(list2)


"""

Code Challenge
  Name: 
    Regular Expression 3
  Filename: 
    regex3.py
  Problem Statement:
    You and Virat are good friends. 
    Yesterday, Virat received credit cards from ABCD Bank. 
    He wants to verify whether his credit card numbers are valid or not. 
    You happen to be great at regex so he is asking for your help!

    A valid credit card from ABCD Bank has the following characteristics:

    It must start with a '4', '5' or ' 6'.
    It must contain exactly 16 digits
    It must only consist of digits (0-9)
    It may have digits in groups of 4, separated by one hyphen "-"
    It must NOT use any other separator like ', ' , '_', etc
    It must NOT have 4 or more consecutive repeated digits 
 
  Hint: 
    Using Regular Expression 
  Input:
    4123456789123456
    5123-4567-8912-3456
    61234-567-8912-3456
    4123356789123456
    5133-3367 -8912-3456
    5123 - 3567 - 8912 - 3456
  Output:
    Valid
    Valid
    Invalid
    Valid
    Invalid
    Invalid
"""

lis=[]
for i in range(0,6):
    lis.append(input("Enter Number: "))


pattern = '^([4-6][0-9]{3})[\-]?([0-9]){4}[\-]?([0-9]){4}[\-]?([0-9]){4}$'

for i in lis:
    result = re.match(pattern,i)
    if result:
        print('Valid')
    else:
        print('Invalid')


"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

"""
 
#list = ['anshul','Anshul','mehta','Mehta']
#list.sort()

list1=[]
list2=[]

pattern = '^([a-zA-Z0-9_\-]+)@([a-zA-Z0-9]+)\.([a-zA-Z]){2,4}$'


for i in range(0,3):
    list1.append(input('Email Address: '))
    
for i in list1:
    result = re.match(pattern,i)
    if result:
        list2.append(i)
        print('True')
    else:
        print('False')
        
list2.sort()
print(list2)


"""

Code Challenge
  Name: 
    Simpsons Phone Book
  Filename: 
    simpsons.py
  Problem Statement: (simpsons_phone_book.txt)
    There are some people with the surname Neu. 
    We are looking for a Neu, but we don't know the first name, 
    we just know that it starts with a J. 
    Let's write a Python script, which finds all the lines of the phone book, 
    which contain a person with the described surname and a first name starting with J. 
 Hint: 
     Use Regular Expressions 
"""

pattern = '^J[a-z]+\sNeu$'

#pattern = 'Neu'

st = 'James Neu'

result = re.match(pattern,st)

if result:
    print('True')
else:
    print('False')

"""

Code Challenge
  Name: 
    Post Codes UK
  Filename: 
    postcodes_uk.py
  Problem Statement:
    We write an expression, which is capable of recognizing the postal codes or postcodes of the UK.

    Postcode units consist of between five and seven characters, 
    which are separated into two parts by a space. 
    
    The two to four characters before the space represent the so-called outward 
    code or out code intended to direct mail from the sorting office to the delivery office. 
    
    The part following the space, which consists of a digit followed by two uppercase characters, 
    comprises the so-called inward code, which is needed to sort mail at the final delivery office. 
    
    The last two uppercase characters do not use the letters CIKMOV, 
    so as not to resemble digits or each other when hand-written.

    The outward code can have the form: One or two uppercase characters, 
    followed by either a digit or the letter R, 
    optionally followed by an uppercase character or a digit. 
    (We do not consider all the detailed rules for postcodes, 
    i.e only certain character sets are valid depending on the position 
    and the context.)    
  Hint: 
    Using Regular Expression 
  Input:
      example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]

"""
 example_codes = {"SW1A 0AA": 'House of Commons',
                 "SW1A 1AA": 'Buckingham Palace',
                 "SW1A 2AA": 'Downing Street',
                 "BX3 2BB": 'Barclays Bank',
                 "DH98 1BT": 'British Telecom',
                 "N1 9GU": 'Guardian Newspaper',
                 "E98 1TT": 'The Times',
                 "TIM E22": 'a fake postcode',
                 "A B1 A22": 'not a valid postcode',
                 "EC2N 2DB": 'Deutsche Bank',
                 "SE9 2UG":  'University of Greenwhich',
                 "N1 0UY": 'Islington, London',
                 "EC1V 8DS": ' Clerkenwell, London',
                 "WC1X 9DT": 'WC1X 9DT',
                 "B42 1LG": 'Birmingham',
                 "B28 9AD": ' Birmingham',
                 "W12 7RJ": ' London, BBC News Centre',
                 "BBC 007" : 'a fake postcode',
                }


pattern = '^([A-Z][\dRA-Z]{2,4})\s[0-9]{1}[A-Z^CIKMOV]{2}$'

'''result = result = re.match(pattern,"E98 1TT")
if result:
    print('dscd') '''

for key in example_codes:
    result = re.match(pattern,key)
    if result:
        print(example_codes[key])
    else:
        print(example_codes[key])



"""

Code Challenge
  Name: 
    Post Codes Germany
  Filename: 
    postcodes_germany.py
  Problem Statement: (post_codes_germany.txt, zuordnung_plz_ort.csv )
    We have to bring together the information of two files. 
    In the first file, we have a list of nearly 15000 lines of post codes with the 
    corresponding city names plus additional information. 

    The other file contains a list of the 19 largest German cities. 
    Each line consists of the rank, the name of the city, the population, 
    and the state (Bundesland): 
    
    Our task is to create a list with the top 19 cities,
    with the city names accompanied by the postal code. 
    If you want to test the following program, 
    you have to save the list above in a file called largest_cities_germany.txt 
    and you have to download and save the list of German post codes

  Output:
    The output of this file looks like this, 
    but we have left out all but the first three postal codes for every city: 
    
        Berlin {'10715', '13158', '13187', ...}
        Hamburg {'22143', '22119', '22523', ...}
        München {'80802', '80331', '80807', ...}
        Köln {'51065', '50997', '51067', ...}
        Frankfurt am Main {'65934', '60529', '60308', ...}
        Essen {'45144', '45134', '45309', ... }
        Dortmund {'44328', '44263', '44369',...}
        Stuttgart {'70174', '70565', '70173', ...}
        Düsseldorf {'40217', '40589', '40472', ...}
        Bremen {'28207', '28717', '28777', ...}
        Hannover {'30169', '30419', '30451', ...}
        Duisburg {'47137', '47059', '47228', ...}
        Leipzig {'4158', '4329', '4349', ...'}
        Nürnberg {'90419', '90451', '90482', ...}
        Dresden {'1217', '1169', '1324', ...}
        Bochum {'44801', '44892', '44805', ...}
        Wuppertal {'42109', '42119', '42287', ...}
        Bielefeld {'33613', '33607', '33699', ...}
        Mannheim {'68161', '68169', '68167', ...}
      
  Hint: 
    Using Regular Expression 
    zuordnung_plz_ort.csv
    list of nearly 15000 lines of post codes with the corresponding city names 
    plus additional information.

"""
import pandas as pd
import requests as re

url = 'https://en.wikipedia.org/wiki/List_of_cities_in_Germany_by_population'

html = re.get(url).content 

data = pd.read_html(html)

new_data = data[0].head(20)


new_data.drop([5,6,7,8],axis=1,inplace=True)
new_data.drop([4],axis=1,inplace=True)


new_data.columns = ['Rank','City','State','Population']

new_data.drop([0],axis=0,inplace=True)

new_data.isna()

#new_data.to_csv('New Microsoft Excel Worksheet.csv', sep='\t', encoding='utf-8')

germany_post_code_data = pd.read_csv('zuordnung_plz_ort.csv')

germany_post_code_data.columns = ['ID','City','Post_Code','State']


list_ = list(new_data['City'])

new_list = []

with open('C://Users//PRINCE//Desktop//Forks_Internship_Work//Code_Challenge//Regular_Expression//zuordnung_plz_ort.csv',"r",encoding="utf8") as f:
    for line in f:
        l = line.split(',')
        new_list.append(l)
 


dict_ = {}
l1=[]
l2=[]


for i in list_:
    for j in new_list:
        if i == j[1]:
            l1.append(j[2])
            l2=l1[:]
            dict_[i]=l2
    del  l1[:]


for key in dict_:
    print(key+"{",dict_[key],"}")
    
    

''' Using GroupBy method of pandas '''

merged_data = pd.merge(new_data,germany_post_code_data,on='City')

merged_data.drop(['Rank','State_x','Population','ID','State_y'],axis=1,inplace=True)

merged_data['Post_Code'] = merged_data['Post_Code'].apply(str)

new_merged_data = merged_data.groupby('City')['Post_Code'].apply(','.join).reset_index()

print(new_merged_data.to_dict())

    











