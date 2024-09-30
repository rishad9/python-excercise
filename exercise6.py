#6. Functions
#1. Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters. Write a main program that
# rolls the dice until the result is 6.
# The main program should print out the result of each roll.
import math
from itertools import count
from random import random, randint
'''
def diceRoll():
    getScore = randint(1,6)
    return getScore
def main():
    count = 0
    while True:
        score = diceRoll()
        if score == 6:
            print("Finally you got score 6")
            break
        count+=1
        print(f"{count}: {score}")
main()
'''

#2. Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice.
# The difference to the last exercise is that the dice rolling in the main program continues until
# the program gets the maximum number on the dice, which is asked from the user at the beginning.
'''
def diceRoll(sides):
    getScore = randint(1, sides)
    return getScore

def main():
    sides = int(input("Enter the number of sides on the dice: "))
    maxNumber = sides
    roll = 0
    while roll != maxNumber:
        roll = diceRoll(sides)
        print(f"Rolled: {roll}")
main()

'''
#3. Write a function that gets the quantity of gasoline in American gallons and returns the
# number converted to litres.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters.
# The conversion must be done by using the function. Conversions continue until the user inputs a
# negative value.
'''
def gallonToLiters(gallons):
    liters = gallons * 3.78541
    return liters
def main():
    while True:
        gallons = float(input("Enter the volume in gallons or negative value to quit: "))
        if gallons < 0:
            break
        liters = gallonToLiters(gallons)
        print(f"{gallons} gallons is equal to {liters:.2f} liters.\n")
main()
'''

# 4. Write a function that gets a list of integers as a parameter.
# The function returns the sum of all the numbers in the list.
# For testing, write a main program where you create a list, call the function, and print out
# the value it returned.
'''
def generateList():
    list = []
    while True:
        userInput = input("Enter a number: ")
        if userInput == "":
            break
        else:
            userInput = int(userInput)
            list.append(userInput)
    return list
def sumOfList(list):
    totalSum = 0
    for i in range(len(list)):
        totalSum += list[i]
    return totalSum
def main():
    list = generateList()
    totalSumList = sumOfList(list)
    print(list)
    print(totalSumList)
main()
'''
#5. Write a function that gets a list of integers as a parameter.
# The function returns a second list that is otherwise the same as the original list except that
# all uneven numbers have been removed.
# For testing, write a main program where you create a list, call the function, and then print out both
# the original as well as the cut-down list.
'''
def generateList():
    list = []
    while True:
        userInput = input("Enter a number: ")
        if userInput == "":
            break
        else:
            userInput = int(userInput)
            list.append(userInput)
    return list
def removeOdd(list):
    evenList = []
    for i in range(len(list)):
        if  list[i]% 2 == 0:
            evenList.append(list[i])
    return evenList
def main():
    firstList = generateList()
    secondList = removeOdd(firstList)
    print(f"generated List is: {firstList}")
    print(f"list of odd number from the list {secondList}")
main()
'''
#6. Write a function that receives two parameters: the diameter of a round pizza in centimeters and
# the price of the pizza in euros. The function calculates and returns the unit price of the pizza per square meter.
# The main program asks the user to enter the diameter and price of two pizzas and tells the user
# which pizza provides better value for money (which of them has a lower unit price).
# You must use the function you wrote for calculating the unit prices.
'''
def calculateUnitPricePizza(diameterCm, priceEuros):
    diameterM = diameterCm/100
    radiusM = diameterM/2
    areaM2 = math.pi*radiusM**2
    unitPricePerM2 = priceEuros/areaM2
    return unitPricePerM2
def main():
    diameterCmPizza1 = float(input("Enter the diameter first pizza in cm: "))
    priceEuros1 = float(input("Enter the price of first pizza in euros: "))
    diameterCmPizza2 = float(input("Enter the diameter second pizza in cm: "))
    priceEuros2 = float(input("Enter the price of second pizza in euros: "))

    unitPrice1 = calculateUnitPricePizza(diameterCmPizza1, priceEuros1)
    unitPrice2 = calculateUnitPricePizza(diameterCmPizza2, priceEuros2)

    print(f"Unit price per square meter for the first pizza: {unitPrice1: .2f} euros/m2")
    print(f"Unit price per sqaure for the second pizza: {unitPrice2:.2f} euros/m2")

    if unitPrice1 < unitPrice2:
        print("The first pizza offers better value for money.")
    else:
        print("The second pizza offers better value for money.")
main()
'''