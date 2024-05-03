#!/usr/bin/env python3

def admin_login(username, password):
    if username.lower() == "admin" and password == "12345":
        return "Access granted"
    else:
        return "Access denied"
    
def hows_the_weather(temperature):
    '''
    Write a function hows_the_weather() that takes in one argument, a temperature.
      If the temperature is below 40, return "It's brisk out there!". 
      If the temperature is between 40 and 65, return "It's a little chilly out there!".
      If the temperature is above 85, return "It's too dang hot out there!". 
      Otherwise, return "It's perfect out there!"
    '''
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else: 
        return "It's perfect out there!"







def fizzbuzz(num):
    '''
    For multiples of three, return "Fizz" instead of the number. 
    For the multiples of five, return "Buzz". 
    For numbers which are multiples of both three and five, return "FizzBuzz". 
    For all other numbers, just return the number itself.
    '''
    if (num % 3 == 0 and num % 5 == 0):
        return "FizzBuzz"
    elif (num % 5 == 0 ):
        return "Buzz"
    elif (num % 3 == 0 ):
        return "Fizz"
    else: return num









def calculator(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        # Check if num2 is not zero to avoid division by zero error
        if num2 != 0:
            return num1 / num2
        else:
            print("Cannot divide by zero!")
            return None
    else:
        print("Invalid operation!")
        return None
