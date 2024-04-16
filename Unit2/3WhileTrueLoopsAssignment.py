# ========== 2.3.1 ==========
# Print("hi")
# while True: 
#    go = input("Shall we continue? ")
#    print("hi")
    
#    if go == "no": 
#        print("Okay, bye.")
#        break

        


# ========== 2.3.2 ==========
# while True:
#        from math import sqrt 
#        integer = int(input("Enter an integer, type 0 to STOP: "))
#        if integer < 0: 
#            print("Invalid number")
#        elif integer == 0: 
#            print("Exiting...")
#            break
#        else: 
#            print(sqrt(integer))
        
# ========== 2.3.3 ==========
# number = 5
# print("Countdown!")
# while True:
#    print(number)
#    number += -1
#    if number == 0:
#        print("Now!")
#        break

# ========== 2.3.4 ==========
# passw = input("Please enter a password: ")
# while True: 
#     passR = input("Repeat password: ") 
#     if passw == passR: 
#         print("User account created!")
#         break
#     else: 
#         print("Those do not match!")
    
# ========== 2.3.5 ==========
# pinR = 4321
# numb = 0
# while True:
#     pinU = int(input("ENTER PIN: "))
#     if pinU != pinR: 
#         numb += 1
#         print("Incorrect.")
#         print(numb)
#     else:
#         numb += 1
#         if numb == 1: 
#             print("Correct! It only took you a single try!")
#             break
#         else: 
#             print("Correct! It took you", numb, "tries.")
#             break

# ========== 2.3.6 ==========
# year = int(input("Year: "))
# year2 = 0
# year3 = 0
# while True: 
#     year3 += 4
#     if year3 >= (year-3): 
#         if year % 4 == 0: 
#          year2 = year + 4
#          print("The next leap year is", year2)
#          break
#         else: 
#             year3 += 4
#             year2 = year3 - year
#             year = year + year2
#             print("The next leap year is", year)
#             break

# ========== 2.3.7 ==========
# sentence = ""
# word = ""
# while True: 
#    sentence += " " + word
#    word = input("Enter a word, type (end) to END: ")
   
#    if word == "end": 
#     print(sentence)
#     break 

# ========== 2.3.8 ==========
# sentence = ""
# word = ""
# word2 = ""
# while True: 
#    sentence += " " + word
#    word = input("Enter a word, type (end) to END: ")

#    if word == "end": 
#     print(sentence)
#     break
#    elif word == word2: 
#      print(sentence)
#      break
#    word2 = word

# ========== 2.3.9 ==========
# numb = 0
# numblist = 0
# numbtype = -1
# numbmean = 0
# numbpos = 0
# numbneg = 0
# while True:
#   numb = int(input("Type in an integer. Type in 0 to finish: "))
#   numblist = (numblist) + (numb)
#   numbtype += 1
#   numbsum = numblist + numb
#   if numb < 0:
#     numbneg += 1
#   if numb > 0: 
#     numbpos +=1
#   if numb == 0: 
#     print("Numbers typed in:",numbtype)
#     print("Sum of numbers:",numbsum)
#     numbmean = numbsum / (numbtype)
#     print("Mean of numbers:", numbmean)
#     print("Positive numbers:", numbpos)
#     print("Negative numbers:", numbneg)
#     break



