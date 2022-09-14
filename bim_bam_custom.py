"""
Bim Bam custom:
    1. Loop through a data structure containing numbers
    and print BimBam result for each
    2. Get user inputs for name and age, tell user the BimBam result
    for their age in a string

BimBam rules:
    - if number is divisible by 3, return "Bim"
    - if number is divisible by 5, return "Bam"
    - if number is divisible by both 3 and 5, return "BimBam"
    - if number is not divisible by either 3 or 5, return the number.
"""


def bim_bam(num):
    """
    Calculate BimBam result
    """
    if num % 2 == 0 and num % 7 == 0:
        result = "BimBam"
    elif num % 2 == 0:
        result = "Bim"
    elif num % 7 == 0:
        result = "Bam"
    else:
        result = num
    return result


def loop_mode():
    """
    Loop through a list of numbers and return the result
    """
    nums = range(1, 101)
    for num in nums:
        print(bim_bam(num))


def custom_mode():
    """
    Get user's name and age, return string to tell them the BimBam result
    for their age
    """
    name = input("What is your name? ")
    age = int(input("How old are you? "))
    result = bim_bam(age)
    print(f"{name}, you are {age} years old. In BimBam, this number would return {result}")


def play():
    """
    Explain modes and let user choose
    """
    print("We have two modes for you to choose from:")
    print("1. Loop through a list of numbers to see what BimBam returns.")
    print("2. Enter your age and see what the BimBam result for that is.")
    mode = int(input("Which would you like to try? (1/2) "))
    if mode == 1:
        loop_mode()
    elif mode == 2:
        custom_mode()
    else:
        print("That is not a recognised option")
        play()


print("Hi there, welcome to BimBam Custom!")
play()
