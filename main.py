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
        r = requests.get(f"http://api.openweathermap.org/data/2.5/find?q={location},US&APPID=b7102f66d17a9d1548feb5470a21746e")
        print("\nSuccessfully connected to openweathmap.org.")
    except:
        print ("Failed to connect.")
        restart = input("(R)estart or (Q)?")
        case = restart.lower()
        if case == "q":
            exit("Goodbye.")
        else:
            main()
    

    data = r.json()
    print (f"\nCurrent weather for {location}" )

    
    temp = ((data['list'][0]['main']['temp']) -273.15) * 9/5 + 32
    temp1 = int(temp)
    print (f"Current temperature: {temp1}.")
    humid = (data['list'][0]['main']['humidity'])
    print (f"Humidity: {humid}%." )
    w = (data['list'][0]['weather'][0]['description'])
    print (f"Clouds: {w}")

    again = input("\nWould you like to see weather for another location? y or n")
    if again == "y":
        main()
    else:
        exit()
    
    


   
    
if __name__ == "__main__":
    main()








    

















            





    
    
        





