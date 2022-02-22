import requests
import json

def get_location():
    '''Get and validate user info'''
    inputIsGood = False
    while inputIsGood == False:
        location = input("Please enter a city name or 5 digit zipcode. ")
        if (location.isnumeric() and len(location) == 5):
            inputIsGood = True
        elif (location.isalpha()):
            inputIsGood = True
        else:
            print ("\nIncorrect city or zip entered.")
            continue
        return location







            





    
    
        





