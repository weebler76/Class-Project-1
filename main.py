import requests
import json


def get_location():
    '''Get city or zip from user'''
    
    location = input("Please enter a city name or 5 digit zipcode. ")
    return location


def run_again():
    '''Ask if user if they want to run again or exit'''
    again = input("\nWould you like to see weather for another location? y or n ")
    print('')
    if again == "y":
        main()
    elif again =="n":
        print('Goodbye.')
        exit()
    else:
        print("Please enter y or n. ")
        run_again()
    
def main():
    #Connect to API and print connection status
    location = get_location()
    try:
        r = requests.get(f"http://api.openweathermap.org/data/2.5/find?q={location},US&APPID=b7102f66d17a9d1548feb5470a21746e")
        print("\nSuccessfully connected to openweathmap.org.\n")
    except:
        print ("Failed to connect.")
        restart = input("(R)estart or (Q)?")
        case = restart.lower()
        if case == "q":
            exit("Goodbye.")
        else:
            main()

#Print weather info
#Try except block to validate user input from get_location function
    data = r.json()
    try:
        temp = ((data['list'][0]['main']['temp']) -273.15) * 9/5 + 32
        temp1 = int(temp)
        print (f"Current temperature: {temp1}.")
        humid = (data['list'][0]['main']['humidity'])
        print (f"Humidity: {humid}%." )
        w = (data['list'][0]['weather'][0]['description'])
        print (f"Clouds: {w}")
    except:
        print(f"{location} is not a valid city or zip code.\n")
        main()

    
    
    run_again()    


   
    
if __name__ == "__main__":
    main()










    

















            





    
    
        





