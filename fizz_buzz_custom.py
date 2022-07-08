"""
Fizz Buzz custom:
    1. Loop through list of numbers and print FizzBuzz result for each
    2. Get user inputs for name and age, tell user the FizzBuzz result
    for their age in a string

FizzBuzz rules:
    - if number is divisible by 3, return "Fizz"
    - if number is divisible by 5, return "Buzz"
    - if number is divisible by both 3 and 5, return "FizzBuzz"
    - if number is not devisible by either 3 or 5, return the number.
"""


def fizzbuzz(num):
    """
    Calculate FizzBuzz result
    """
    if num % 3 == 0 and num % 5 == 0:
        result = "FizzBuzz"
    elif num % 3 == 0:
        result = "Fizz"
    elif num % 5 == 0:
        result = "Buzz"
    else:
        result = num
    return result


def loop_mode():
    """
    Loop through a list of numbers and return the result
    """
    nums = [1, 3, 5, 7, 9, 10, 13, 15, 21, 45]
    for num in nums:
        print(f"In Fizzbuzz, {num} would return {fizzbuzz(num)}")


def custom_mode():
    """
    Get user's name and age, return string to tell them the FizzBuzz result
    for their age
    """
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    result = fizzbuzz(age)
    print(f"{name}, you are {age} years old.")
    print(f"In FizzBuzz, this number would return {result}")


def play():
    """
    Explain modes and let user choose
    """
    print("Hi there, welcome to FizzBuzz Custom")
    print("We have two modes for you to choose from:")
    print("1. Loop through a list of numbers to see what FizzBuzz returns.")
    print("2. Enter your age and see what the FizzBuzz result for that is.")
    mode = int(input("Which would you like to try? (1/2) "))
    if mode == 1:
        loop_mode()
    else:
        custom_mode()


play()
