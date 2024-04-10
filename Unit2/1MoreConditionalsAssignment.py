# print("########## 2.2.1 ##########")

word = str(input("Please type in a word: "))
length = int(len(word))

if length > 1: 
    print("There are",length,"letters in the word",word, ".")
print("thank you!")

# print("########## 2.1.2 ##########")

numb = float(input("Please type in a number: "))
numb2 = int(numb)
numb3 = numb - numb2
print("Integer part:", numb2)
print("Decimal part:", numb3)

# print("########## 2.1.3 ##########")

age = int(input("How old are you? "))
if age < 18:
    print("You may not vote.")
else: 
    print("You may vote!")

# print("########## 2.1.4 ##########")

numb1 = int(input("Please type in number one: "))
numb2 = int(input("Please type in number two: "))
if numb1 > numb2: 
    print("The greater number was", numb1)
elif numb1 < numb2: 
    print("The greater number was", numb2)
else: 
    print("The numbers are equal!")

# print("########## 2.1.5 ##########")

print("Person 1")
p1 = str(input("Name of person 1: "))
a1 = float(input("Age of person 1: "))
print("Person 2")
p2 = str(input("Name of person 2: "))
a2 = float(input("Age of person 2: "))
if a1 > a2: 
    print("The older person is", p1)
elif a2 > a1: 
    print("The older person is", p2)
else: 
    print("The two are the same age.")

# print("########## 2.1.6 ##########")

str1 = str(input("Please enter word 1: "))
str2 = str(input("Please enter word 2: "))
if str1 < str2: 
    print(str2,"comes alphabetically last.")
elif str2 > str1: 
    print(str1,"comes alphabetically last.")
elif str1 == str2: 
    print("You typed the same word twice.") 
