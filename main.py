

import requests
import json

#get city or zip from user 
location = input("Please enter city or zipcode. ")

response= requests.get("http://api.openweathermap.org/data/2.5/find?q=30721&appid=b7102f66d17a9d1548feb5470a21746e")

#tell user if connected
if response.status_code == 200:
    print("connected")

else:
    print("You failed.")

print(response.json())
