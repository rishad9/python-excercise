#5. List Structures and iterative loops(for)
#1. Write a program that asks the user how many dice to roll.
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.
from random import random, randint
'''
numOfDice = int(input("How many dice would you like to roll? "))
totalSumOfDiceRolls = 0
index=0
for index in range(numOfDice):
    roll = randint(1, 6)
    totalSumOfDiceRolls += roll
print(f"The sum of all {numOfDice} dice rolls is {totalSumOfDiceRolls}.")
'''
#2. Write a program that asks the user to enter numbers until they input an empty string to quit.
# At the end, the program prints out the five greatest numbers sorted in descending order.
# Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
'''
numbers = []
while True:
    user_input = input("enter a number or press enter to quit: ")
    if user_input == "":
        break
    try:
        number = float(user_input)
        numbers.append(number)
    except ValueError:
        print("Invalid input, Please enter a valid number.")
numbers.sort(reverse=True)
print("The five greatest numbers are:", numbers[:5])
'''
#3. Write a program that asks the user for an integer and tells if the number is a prime number.
# Prime numbers are number that are only divisible by one or the number itself.
#For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
#On the other hand, 21 is not a prime number as it is divisible by 3 and 7.
'''
while True:
    userInput = int(input("enter a number or press enter to quit: "))
    isPrime = True
    if userInput < 2:
        isPrime = False
    else:
        for i in range(2, userInput):
            if userInput % i == 0:
                isPrime = False
                break
    if isPrime:
        print(f"{userInput} is a prime number.")
    else:
        print(f"{userInput} is not a prime number.")

'''

#4. Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
# and stores them into a list structure.
# Finally, the program prints out the names of the cities one by one, one city per line, in the same order they were read as input.
# Use a for loop for asking the names and a for/in loop to iterate through the list.

cityList = []
for i in range(0,5):
    userInput = input("enter the name of city you know: ")
    if userInput == "":
        break
    else:
        cityList.append(userInput)
    i+=1
for city in cityList:
    print(city)


