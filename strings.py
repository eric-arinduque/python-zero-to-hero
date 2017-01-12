'''
Eric Arinduque
MVA - Introduction to Python - Strings
https://mva.microsoft.com/en-US/training-courses/introduction-to-programming-with-python-8360?l=fxpo9xFz_5704984382

Example 1: Comments

# Collect first name from user
firstName = input("What is your first name? ")

lastName = input("What is your last name? ")

country = input("What country are you from? ")
country = country.upper()

# Create a friendly output
# /n means print on a new line
print("\nHello " + firstName + " " + lastName + " from " + country + ".")

Example 2: Input from user

animal = input("What is your favorite animal? ")
building = input("Name a famous building? ")
color = input("What is your favorite color? ")
print("Hickory Dickory Dock!")
print("The " + color + " " + animal + " ran up the " + building + ".")

Example 3: Manipulate input from user

message = 'Hello World'
print(message.lower())
print(message.upper())
print(message.swapcase())

Example 4: More string functions
'''
message ='hello world'
print(message.find('world')) 
print(message.count('o'))
print(message.capitalize()) 
print(message.replace('hello','Hi'))

