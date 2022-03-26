#First we import the necessary modules
import os
import sys
import time
#the most important module is os and the request module
import requests
#we use the requests module to get the data from the API
#we use the json module to parse the data
import json
#lets start of by creating a variable to store the api url
#we will use a fake json api to get the data
api_url = "https://jsonplaceholder.typicode.com/"
#then we create multiple functions to get data from all the different endpoints
#first one will be users
def get_users():
    api_url = "https://jsonplaceholder.typicode.com/users"
    #we use the get method to get the data
    response = requests.get(api_url)
    #we use the json method to parse the data
    data = response.json()
    #we return the data
    return data
#last but not least we create a function to get the photos
def get_photos():
    api_url = "https://jsonplaceholder.typicode.com/photos"
    #we use the get method to get the data
    response = requests.get(api_url)
    #we use the json method to parse the data
    data = response.json()
    #we return the data
    return data
#now to create a main function
def main():
    print("Select a choice:")
    print("1. Get Users")
    print("2. Get Photos")
    print("3. Exit")
    #we create a variable to store the choice
    choice = int(input("Enter your choice: "))
    #we use a while loop to keep the program running
    while True:
        #we use a if statement to check the choice
        if choice == 1:
            #we use the get_users function to get the data
            data = get_users()
            #we use a for loop to print the data
            for user in data:
                print(user)
            #we use a break statement to break the loop
            break
        elif choice == 2:
            #we use the get_photos function to get the data
            data = get_photos()
            #we use a for loop to print the data
            for photo in data:
                print(photo)
            #we use a break statement to break the loop
            break
        elif choice == 3:
            #we use the break statement to break the loop
            break
        else:
            #we use the print statement to print an error message
            print("Invalid choice")
            #we use the break statement to break the loop
            break
#now we use the main function to run the program
if __name__ == "__main__":
    main()