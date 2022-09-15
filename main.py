# importing required dependencies/libraries
import csv

import requests
import os
from datetime import datetime

# read api key store in file for security
user_api = open('api_key', 'r'). read()

# create and format user input for location variable
location = input("Enter the city or country name: ")
loc = format(location.upper())

# create api link to handle requests and responses
complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# create additional variables to store from api request
temp_city = ((api_data['main']['temp']) - 273.15)
temp_city1 = "{:.2f}°C".format(temp_city)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
hmdt1 = "{:.0%}%".format(hmdt)
wind_spd = api_data['wind']['speed']
date_time1 = datetime.now().strftime("%d %b %Y")
date_time2 = datetime.now().strftime("%I %M %S %p")

# create csv file that would display stored data using variables above
with open('weather.csv', 'w', newline='') as csvfile:
    fieldnames = ['City|Country', 'Date', 'Time', 'Temperature', 'Weather Desc', 'Humidity (%)', 'Wind Speed (k/mph)']
    thewriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    thewriter.writeheader()
    thewriter.writerow({'City|Country': loc, 'Date': date_time1, 'Time': date_time2, 'Temperature': temp_city1, 'Weather Desc': weather_desc,
    'Humidity (%)': hmdt, 'Wind Speed (k/mph)': wind_spd})





