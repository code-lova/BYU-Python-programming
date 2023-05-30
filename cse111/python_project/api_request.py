#A program that retrieves data from a a server on the internet. 
#The Python requests module contains functions that retrieve data from a server.
#Using Pandas to export all the data we collected
#from the API request we made from the server to a CSV file.

import requests
import pandas as pd



baseurl = "https://rickandmortyapi.com/api/"
endpoint = "character"

def main():
    try: 
        main_list = []
        
        data = main_request(baseurl, endpoint, 1)

        
        #getting the number of pages starting from 1 instead of 0
        for x in range(1, get_pages(data)+1):
            print(x)
            
            #Adding the charecter list into a main list we use extend function 
            #cause we are appending a list to another list
            main_list.extend(get_parse_json_data(main_request(baseurl, endpoint, x))) 
        
        #Exporting the data from the the API call to a CSV file.
        new_data_frame = pd.DataFrame(main_list)
        new_data_frame.to_csv("characters.csv", index=False)
            
            
            
        #print(new_data_frame.head(), new_data_frame.tail())
        #print(main_list)   
        #print(get_parse_json_data(response = data))
        #get_num_of_pages = get_pages(response = data)
        
    except ConnectionRefusedError as conn_err:
        # This code will be executed if the user enters the name
        # of a file and doesn't have permission to read that file.
        print()
        print(type(conn_err).__name__, conn_err, sep=": ")
        print(f"SORRY.!! You are not connected to the internet.")
    
    except Exception as excep:
        # This code will be executed if some
        # other type of exception occurs.
        print()
        #print(type(excep).__name__, excep, sep=": ")
        print("Please Connect To The Interent, Then Run the Program Again..")
        
        
    
    pass


def main_request(baseurl, endpoint, x):
    """Make a get request to an API endpoint to get information

    Args:
        baseurl (url): The API url of which we are getting the informaton
        endpoint (string): what part of the information we want.
        x (string): This represent the page number

    Returns:
        json data: List of data with Json format encoded
    """
    
    make_request = requests.get(baseurl + endpoint + f'?page={x}')
    
    return make_request.json()



def get_pages(response):
    """getting the number of pages from the API endpoint information 
    'character'

    Args:
        response (data): number of pages 

    Returns:
        integer: The number of pages 
    """
    
    pages = response["info"]["pages"]
    
    return pages
    
    

def get_parse_json_data(response):
    """getting the names of each character in the movie and the number 
    of eposides they are present in from the response when we initiate an API call with 
    a reques to get content.

    Args:
        response (json data): response
    Return: A compound list of characters 
    """
    character_list = []
    for each_data in response["results"]:
        
        characters = {
            'id': each_data["id"],
            'name': each_data["name"], 
            'num_of_episodes': len(each_data["episode"]),
        }
        
        character_list.append(characters)
        
    return character_list





# If this file is executed like this:
# > python requst.py
# then call the main function. However, if this file is simply
# imported (e.g. into a test file), then skip the call to main.   

if __name__ == "__main__":
    main()
    




# name = data["results"][0]["name"]

# episodes = data["results"][0]["episode"]

#Some randon free API we can get data from and work with
#in a list 

# loc = get('https://api.coincap.io/v2/assets')
# print(loc.json())


# # from requests import get

# # loc = get('https://ipapi.co/102.177.160.0/json/')
# # print (loc.json())


# # loc = get('http://ip-api.com/json/facebook.com')
# # print (loc.json())


