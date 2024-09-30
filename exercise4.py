from random import randint, random, choice

#Exercise 1
'''
sum = 0
counter = 1
while counter<10:
     sum = sum + counter
     print(f"the counter, {counter}, and  the sum of the counter is {sum}")
     counter = counter + 1
'''


#Exercise 2
'''
i = 1
n = int(input("Enter a limit: "))
while i<=n:
    if i%2==0:
        print(f"the even number is {i}")
    elif i%2!=0:
        print(f"the odd number is {i}")
    i = i+1
'''

#Exercise 3
'''
target_number = randint(1, 10)
counter = 0
while True:
    user_guess = int(input("Guess a number between 1 and 9: "))
    if user_guess == target_number:
        print("Well guessed")
        break
    else:
        print("Try again")
    counter = counter + 1
    print("tried", counter)
'''
#Exercise 4
'''
user_input = ""
while user_input =="":
    user_input = input("press enter to exit or type something to display")
    print("You typed", user_input)
'''

#Exercise 5
'''
#Initialize the result by flipping the coin once
result = choice(["Head","Tail"]).lower()
#flip the coin until we get head
while result != "head":
    print("flipped", result)
    #flip the coin again
    result = choice(["Head","Tail"]).lower()
#Print the final result when 'Heads" is obtained
print("Finally, flipped", result)
'''
#4. While loops(while)
#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
'''
range_object = range(1,1000)
index = 0
while index < len(range_object):
    value = range_object[index]
    if value % 3 == 0:
        print(f"The number is divisible by 3 {value}")
    index += 1
'''

#Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.
'''
input_inches  = float(input("Enter a positive number in inches: "))
while input_inches > 0:
    centimeter = input_inches * 2.54
    print(f"the entered{input_inches}inches is {centimeter} centimeter")
    input_inches = float(input("Enter a positive number in inches: or 0 to quit"))

'''

#Write a program that asks the user to enter numbers until they enter an empty string to quit.
#Finally, the program prints out the smallest and largest number from the numbers it received.
'''
input = input("Enter a number: ")
list = []
while input !="":
    list.append(input)
    list = int(input("Enter next number: "))
print(list)
'''

#Lecture: kirpal
#List
#Example1
'''
names =[]
name = input("Enter a name or quit by pressing enter ")
while name != "":
    names.append(name)
    name = input("Enter a next name or quit by pressing enter ")
print(names)

'''
#Example2
'''
list1 = ["duxin","hechun","sailesh"]
list2 =["dog","cat","ssds"]
list1.extend(list2)
list2.extend(list1)
print(list1)
print(list2)
list2.sort()
print(list2)

'''

#For loop
#Example1
'''
for number in range(5,23,3):
    print(number)
'''
#Example2
'''
names = ["a","b","c"]
for n in names:
    print(n)
'''
#Example 3
'''
for n in range(1,11,1):
    print(f"2*{n}= {2*n}")
'''

#Example4
'''
num = int(input("Enter a number: "))
for n in range(1,num+1):
    if n%2==0:
        print(f"The even number is {n}")
    else:
        print(f"The odd number is {n}")
'''
