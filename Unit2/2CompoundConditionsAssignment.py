print("########## 2.2.1 ##########")
age = int(input("What is your age? "))
if age < 5: 
    if age < 0: 
        print("That sounds wrong.")
    else: 
        print("I suspect you cannot write yet..")
else: 
    print("Okay, you're", age,"years old.")

# print("########## 2.2.2 ##########")
name = input("What's your name? ")
if name == "huey" or name == "dewey" or name == "louie": 
    print("I think you may be one of Donald Duck's nephews!")
elif name == "morty" or name == "ferdie":
    print("I think you may be one of Mickeey Mouse's nephews!")
else: 
    print("Youre not a nephew of anyone I know.")

# print("########## 2.2.3 ##########")
grade = float(input("Type in percent grade here: "))
if grade >=0 and grade <=59: 
    print("Grade: F")
elif grade >=60 and grade <=69: 
    print("Grade: D")
elif grade >=70 and grade <=79: 
    print("Grade: C")
elif grade >=80 and grade <=89: 
    print("Grade: B")
elif grade >=90 and grade <=100:
    print("Grade: A") 
else: 
    print("Impossible!")

# print("########## 2.2.4 ##########")
numb = int(input("Enter number here: "))
if numb % 5 == 0 and numb % 3 == 0: 
    print("Fizzbuzz")
elif numb % 3 == 0:
        print("Fizz")
elif numb % 5 == 0: 
    print("Buzz")

# print("########## 2.2.5 ##########")
year = int(input("Please enter a year: "))
if year % 4 == 0: 
    if year % 100 == 0: 
    
        if year % 400 == 0:
            print ("That is a leap year!")
        else: 
            print("That is NOT a leap year.")
    else: 
        print("That is a leap year!")
else: 
    print("That is NOT a leap year.")

# print("########## 2.2.6 ##########")
lett1 = input("letter one: ")  #a
lett2 = input("letter two: ")  #b
lett3 = input("letter three: ")  #c
if (lett1 < lett2 and lett1 > lett3) or (lett1 < lett3 and lett1 > lett2): 
    print(lett1,"is in the middle.")
elif (lett1 > lett2 and lett2 > lett3) or (lett1 < lett2 and lett2 < lett3): 
    print(lett2, "is in the middle.")
elif lett1 == lett2 and lett1 == lett3: 
    print("Those are all the same letter!")
else: 
    print(lett3, "is in the middle.")