
print("########## 1.5.1 ##########")
year = int(input("Please type in a number: "))
if year == 1984: 
    print("Orwell")

print("########## 1.5.2 ##########")
numb = int(input("Please type in a number: "))
if numb < 0: 
    numb = numb * -1
print ("The absolute value is", numb)

print("########## 1.5.3 ##########")
name = str(input("What is your name? "))
if name != "Jerry": 
    number = int(input("How many portions of soup? "))
    number = number * 5.90 
    print("The total cost is", number)
print ("Next, please!")

print("########## 1.5.4 ##########")
number = int(input("please type in a number: "))
if number < 1000: 
    print("This number is less than 1000")
if number < 100:
    print ("This number is less than 100")
if number < 10: 
    print("This number is less than 10")
print("Thank you!")

print("########## 1.5.5 ##########")
numb1 = float(input("Please enter number 1: "))
numb2 = float(input("Please enter number 2: "))
oper = input("Please enter your desired operation: ")

if oper == "add": 
    numb3 = numb1 + numb2
    print(numb1,"+",numb2,"=", numb3)

if oper == "subtract": 
    numb3 = numb1 - numb2
    print(numb1,"-",numb2,"=", numb3)

if oper == "multiply": 
    numb3 = numb1 * numb2
    print(numb1,"*",numb2,"=", numb3)

if oper == "divide": 
    numb3 = numb1 / numb2
    print(numb1,"/",numb2,"=", numb3)

print("########## 1.5.6 ##########")
temp = float(input("Please type in a temperature (F): "))
temp2 =float(0.5556 * (temp - 32))
print (temp, "Degrees Farenheit equals",temp2, "Degrees Celsius.")
if temp2 < 0: 
    print("Brr! It's cold in here!")


print("########## 1.5.7 ##########")
wage = float(input("Hourly wage: "))
hours = float(input("Hours worked: "))
day = str(input("Day of the week: "))
daily = wage * hours
if day == "Sunday": 
    daily = daily * 2
print("Daily wages:", daily)

print("########## 1.5.8 ##########")
# Fix the program
points = int(input("How many points are on your card? "))
if points < 100:
    points2 = points * 1.1
    print("Your bonus is 10 %")

if points >= 100:
    points2 = points * 1.15
    print("Your bonus is 15 %")

print("You now have", points2, "points")

print("########## 1.5.9 ##########")
print("What is the weather forecast for tomorrow? ")
temp = float(input("What is the temperature? "))
rain = str(input("Will it rain? "))
print ("Wear jeans and a tee shirt.")
if temp < 20: 
    print("I recommend a sweater as well.")
if temp < 10: 
        print ("Take a jacket with you too.")
if temp < 5: 
    print ("Actually, make it a warm coat.")
    print ("I think gloves are in order!")

if rain == "yes": 
        print("Don't forget your umbrella!")
 
    
