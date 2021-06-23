from os import read
import requests
from datetime import datetime

api_key = '9d2ebd2dac5e101375bbf2f40446fe84'  
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y || %I:%M:%S %p")

print("++++++++++++++++++++++++++")
print("  Current weather Status of city - {} || {}".format(location.upper(), date_time))
print("++++++++++++++++++++++++++")
print("   Current temperature is      : {:.2f} deg C".format(temp_city))
print("   Current weather description :", weather_desc)
print("   Current Humidity            :", hmdt, '%')
print("   Current wind speed          :", wind_spd, 'kmph')

f = open("weather report.txt","a")
f.write("+++++++++++++++++++++++++\n")
f.write("  Weather history for city - {} || {}\n".format(location.upper(), date_time))
f.write("+++++++++++++++++++++++++\n")
f.write('Current temperature is      : {:.2f} deg C\n'.format(temp_city))
f.write('Current weather description : {:} \n'.format(weather_desc))
f.write('Current Humidity            : {:.0f} %\n'.format(hmdt))
f.write('Current wind speed          : {:} kmph\n'.format(wind_spd))
f = open("weather report.txt","r")
print("\n Older weather search records are-\n")
print(f.read())
f.close()