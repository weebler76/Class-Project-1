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
        
def main():
    location = get_location()
    try:
        response = requests.get(f"htttp://api.openweathermap.org/data/2.5/find?q={location},US&APPID=b7102f66d17a9d1548feb5470a21746e")
        print("Successfully connected to openweathmap.org.")
    except:
        print ("Failed to connect.")
        restart = input("(R)estart or (Q)?")
        case = restart.lower()
        if case == "q":
            print (case)
        elif case == "r":
            print(case)
        else: 
            print ("Gotta figure this one out.")
            
        
        


    







if __name__ == "__main__":
    main()

    

















            





    
    
        





