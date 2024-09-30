#Conditionals
# Example1
'''
age = int(input("Enter age: "))
if 15 <= age < 18:
    weight = float(input("Enter weight (kg): "))
if (age >=18 or age>=15 and weight >=55):
    print("The medicine can be used.")
'''

#Example2
'''
score = float(input("Enter score: "))
if score > 90:
    print("A1")
elif score>80:
    print("A2")
elif score>70:
    print("B1")
elif score>60:
    print("B2")
elif score>50:
    print("C1")
elif score>40:
    print("C2")
'''

#Example3
'''
wheels = int(input("Enter number of wheels: "))

if wheels == 2  :
    print("This is a bicycle")
    battery = input("Enter type of vehicle with battery yes/no")
    if (battery == "yes"):
        print("This E-bike with battery")
    else:
        print ("wrong input")
elif wheels ==2 and type == "battery" :
    print("This is a E-bicycle")
elif wheels ==3 :
    print("This is a tricycle")
elif wheels ==4 :
    print("This is a car")
elif wheels > 4 :
    print("This is not such vehicle")
'''
#Example4
'''
age = int(input("Enter age: "))
if age>=65:
    print("You are now retired")
elif 18<=age :
    print("Working age")
elif 7<=age<=17:
    print("You are now studying")
elif 0<=age<=6 :
    print("You are a Child")
'''
#Exercise 3.1
'''
length = float(input("Enter the length of a zander in centimeters"))
if (length>=42):
    print("The zander meets the size limit, you can keep it")
else:
    print("The zander does not meet the size limit")
    print("The zander was", 42 - length, "centimeters below the size limit.")

'''
#Exercise 3.2
'''

cabinClass = input("Enter cabin class of a cruise ship, LUX/A/B/C ")
if cabinClass =="LUX":
    print("Upper deck cabin with balcony")
elif cabinClass=="A":
    print("Above the car deck, equipped with a window.")
elif cabinClass=="B":
    print("windowless cabin above the car deck.")
elif cabinClass == "C":
    print("windowless cabin above the car deck.")
else:
    print("Invalid cabin class")

'''
#Excersice 3.3
'''
gender = input("Enter your gender: Male/Female")
if gender == "male":
    hemoglobin = float(input("Enter the hemoglobin value g/l"))
    if hemoglobin < 134:
        print(f"The {gender}hemoglobin level is low")
    elif 134<=hemoglobin<=167:
        print(f"The {gender}hemoglobin level is normal")
    elif hemoglobin > 167:
        print(f"The {gender}hemoglobin level is high")
elif gender == "female":
    hemoglobin = float(input("Enter the hemoglobin value g/l"))
    if hemoglobin < 117:
        print(f"The {gender}hemoglobin level is low")
    elif 117<=hemoglobin<=155:
        print(f"The {gender}hemoglobin level is normal")
    elif hemoglobin > 155:
        print(f"The {gender}hemoglobin level is high")

'''

#Exercise 3.4
'''
year =""
while year != "exit":
    year = int(input("Enter year or type exit to terminate: "))
    if (year%4 == 0) and (year%100!= 0) or (year%400 ==0):
        print(f"The entered year is a leap year {year}")
    else:
        print(f"The entered year is a non-leap year {year}")
'''