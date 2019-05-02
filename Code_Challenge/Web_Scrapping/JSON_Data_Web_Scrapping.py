"""

Code Challenge
  Name: 
    Student and Faculty JSON
  Filename: 
    student.json
    faculty.json
  Problem Statement:
    Create a student and Faculty JSON object and get it verified using jsonlint.com
    Write a JSON for faculty profile. 
    The JSON should have profile of minimum 2 faculty members. 
    The profile for each faculty should include below information atleast:

        First Name
        Last Name
        Photo (Just a random url)
        Department 
        Research Areas (can be multiple)
        Contact Details (should include phone number and email id and can have multiple )
   Hint:
       www.jsonlint.com
       
"""
''' Valid Json '''

{

	"Faculty": [{
			"First Name": "Anshul",
			"Last Name": "Mehta",
			"Photo": "https://sdsds.com",
			"Department": "x",
			"Research Areas": ["x", "y", "z"],
			"Contact Details": {
				"Mob No.": 8578967410,
				"Email": "wsxedxxccxc@dscf.com"
			}
		},

		{
			"First Name": "fgfdfd",
			"Last Name": "dfgvdfvfcgv",
			"Photo": "https://xyz.com",
			"Department": "A",
			"Research Areas": ["X", "Y", "Z"],
			"Contact Details": {
				"Mob No.": 8529639635,
				"Email": "scsdfdcxc@dscf.com"
			}
		}
	],

	"Student": [{
			"First Name": "plmikn",
			"Last Name": "guhijuhn",
			"Photo": "https://qazpl.com",
			"Branch": "CS",
			"Contact Details": {
				"Mob No.": 7899639635,
				"Email": "plmkin@dscf.com"
			}
		},

		{
			"First Name": "dfgfdfd",
			"Last Name": "dfgvdfvfcgv",
			"Photo": "http://adsds.com",
			"Branch": "EC",
			"Contact Details": {
				"Mob No.": 987637410,
				"Email": "s78sdsxc@dscf.com"
			}
		}
	]

}







"""
Code Challenge
  Name: 
    JSON Parser
  Filename: 
    json.py
  Problem Statement:
    Get me the other details about the city
        Latitude and Longitude
        Weather Condition
        Wind Speed
        Sunset Rise and Set timing
"""

import json

#import bs4 as bs
import requests as re

def print_weather_data(data,city):
    print("Latitude: {} and Longitude: {}".format(data['coord']['lon'],data['coord']['lat']))
    print("Weather Condition: {}".format(data['weather'][0]['main']))
    print("Wind speed: {} m/s".format(data['wind']['speed']))
    print("Sunset Rise: {} and Sunset timing: {}".format(data['sys']['sunrise'],data['sys']['sunset']))
    print("{}'s temperature: {}°C ".format(city,data['main']['temp']))
    print("Description: {}".format(data['weather'][0]['description']))
    
    


url = 'http://api.openweathermap.org/data/2.5/weather?'
api_key = 'b35975e18dc93725acb092f7272cc6b8'

city_name = input("Enter City Name : ")

complete_url = url + "appid=" + api_key + "&q=" + city_name

response = re.get(complete_url)
data = response.json()

try:
    print_weather_data(data,city_name)
except:
    print("City Not Found")











"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""
import json

import requests as re

base_url = "https://free.currconv.com/api/v7/convert?"

currency1 = input("Enter the Currency\n From: ")
currency2 = input("To: ")
api_key = '260970b9c8e40c775dce'

#url = "https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=260970b9c8e40c775dce"

complete_url = base_url + "q=" + currency1 + "_ "+ currency2 + "&apikey=" + api_key

response = re.get(url)

print("Current Currency Conversion Price Form USD to INR is :",response.json())




"""
Code Challenge
  Name: 
    Posting of Data
  Filename: 
    httpbin.py
  Problem Statement:
    Create a client REST API that sends and receives some information from 
    the Server by calling server's REST API.
    You are expected to create two functions each for Sending and 
    Receiving data.
    You need to make two api calls, one with POST method for sending data 
    and the other with GET method to receive data
    All the communication i.e. sending and receiving of data with the 
    server has to be in JSON format
  Hint:
    Host: httpbin.org
    Port :  80
    Protocol : POST
    URI : /post
    Content-Length: 32 

    firstname=Chris&language=English
"""



import requests as re
import json

url_name_1 = 'http://httpbin.org/post'
data = {'firstname':'Chris','language':'English'}
#j_data = json.dumps(data)
#r = re.post(url = url_name , data = j_data, headers = {"Content-Type":"application/json"})

''' Post Data Function'''
def post_data(url,data):
    r1 = re.post(url = url_name_1 , json = data)
    post_data = r1.json()
    return post_data

print("The Data to be post is :",post_data(url_name_1,data))  

''' Get Data '''

url_name_2 = 'http://httpbin.org/get'

def get_data(url,data):
    r2 =re.get(url = url_name_2, params=data)
    get_data = r2.json()
    return get_data

print("The Data to be get is : ",get_data(url_name_2,data))





"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
"""


import requests as re
import pandas as pd

url = 'https://www.icc-cricket.com/rankings/mens/team-rankings/odi'

html = re.get(url).content

df =  pd.read_html(html)

type(df)
type(df[0])

print(df[0])
df[0].to_csv('ICC_Cricket.csv', sep='\t')








