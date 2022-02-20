import json
import os
import csv

print("Welcome to the file system assistant. Here, we can help you create a directory and save a file to that directory. We will also be adding some of your information to that file as well.")

directory = input("What is the name of the directory you would like to save your file in today?")
try:
    #Create Target Directory
    os.mkdir(directory)
    print("Directory " , directory, " Created ")
except FileExistsError:
    print("Directory " , directory , " already exists")
    

fileName = 'filename.json'
try:
    with open(fileName) as f:
        file_name = json.load(f)
except FileNotFoundError:
    file_name = input("What is the name of the file you would like to save?")
    with open(fileName, 'w') as f:
        json.dump(file_name, f)
        print("Thank you. We have now created the file specified")
        
print("Now we just need some information to add onto your file.")

user_info= input("May we have your name, address and phone number?")
with open(fileName, 'a') as csvfile:
    json.dump(file_name, f)
    print("Thank you. We have now added your information to your file.")
    
