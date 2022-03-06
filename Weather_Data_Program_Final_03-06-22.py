## Weather Data for City/Zipcode Program ##
## CIS245-304j; Created by Ahmed Bushra ##

## openweathermap guide for API use: https://openweathermap.org/current ##

## Importing Requests library ##
from urllib import response
import requests

## get_data function will get the data from building URL through user input + API key ##
def get_data(zip=None, city=None):
    ## The base URL for fetching weather data from Openweathermap. Temperature unit change found here: https://openweathermap.force.com/s/article/switching-between-temperature-units-2019-10-24-21-47-24 ##
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    ## Ahmed's personal API key obtained from openweathermap ##
    api_key = "c1aa4f82aea3f3ea0eae5f7916d2fb99"

    ## Building url with user input. "us" is added as the default country to search for both zip & city ##
    if zip is not None:
        base_url += "?zip="+str(zip)+",us"
    else:
        base_url += "?q="+str(city)+",us"
    ## This appends the API key to the rest of the formulated url ##
    base_url += "&appid="+str(api_key)

    ## Requests via requests module ##
    returned_response = requests.get(base_url)

    return returned_response

## display_results will be defined here as a function. This function will parse the queried data into display-able info ##
def display_results(response):

    ## 200 means request was made successfully ##
    if response.status_code == 200:

        data=response.json()

## API response parameters found at https://openweathermap.org/weather-data ##
        print(f"""{data['name']} weather forecast is as follows: 
        The low temp will be {data['main']['temp_min']} degrees 
        The high will be {data['main']['temp_max']} degrees
        There will be {data['weather'][0]['description']} with wind speeds of {data['wind']['speed']}mph
        """)

    else:
## If request fails, it will print the error code for the user ##
        print("Request Failed, Try Again Error Code : ",response.status_code)

    ## Main() is the main function of the program which will take user input and run the loop 
# so users may continue to use the program ##
def main():
    ## While loop with try/except blocks ##
    while True:
        user_input = int(input("Please select one of the following to find weather data: \n1. Search by zip code\n2. Search by city name\n3. Exit\n"))
        if user_input == 1:
            try:
                queried_data=int(input("Enter zip code: "))
                returned_response= get_data(queried_data,None)
                display_results(returned_response)
            except Exception as ex: ## Will show webpage error such as 404 ##
                print("Error : ",ex)
        elif user_input == 2:
            try:
                queried_data = input("Enter city name: ")
                returned_response= get_data(None,queried_data)
                display_results(returned_response)
            except Exception as ex:
                print("Error: ",ex)
        elif user_input==3:
            print("The program will now end. Thank you!\n")
            break
if __name__=="__main__":
    ## Calling main module ##
    main()