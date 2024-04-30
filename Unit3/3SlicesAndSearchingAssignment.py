# ========== 3.3.1 ==========
# string = input("Type in a string: ")
# length = 1
# while length <= len(string): 
#     slice1 = string[0:(length)]
#     print(slice1)
#     length+=1

# ========== 3.3.2 ==========
# string = input("Type in a string: ")
# length = (len(string))-1
# while length >= 0: 
#     slice1 = string[(length): len(string)]
#     print(slice1)
#     length = length -1

# ========== 3.3.3 ==========
# string = input("Enter a string: ")
# if ("o" in string) == True: 
#     print("o found")
# else: 
#     print("o not found")
# if ("e" in string) == True: 
#     print("e found")
# else: 
#     print("e not found")
# if ("a" in string) == True: 
#     print("a found")
# else: 
#     print("a not found")

# ========== 3.3.4 ==========
# string = input("Enter a string: ")
# letter = input("Type in a character: ")
# numb = (string.find(letter))
# numb2 = numb + 3
# slice1 = string[numb:numb2]
# if numb > (len(string) - 3): 
#     print("")
# elif len(string) > 2: 
#     print(slice1)

# # ========== 3.3.5 ==========
string = input("Enter a string: ")
substring = input("Enter a letter: ")
numb1 = (string.find(substring))
end1 = numb1 + 3
type1 = string[numb1:end1]
slice1 = string[numb1+1:]
if numb1 == -1: 
    print("No instance found.")
else: 
    print(type1)
    while True: 
        if len(slice1) <= 2 or numb1 == -1: 
            break
        numb1 = (slice1.find(substring))
        end1 = numb1 + 3
        type1 = slice1[numb1:end1]
        slice1 = slice1[numb1+1:]
        print(type1)
            


# ========== 3.3.6 ==========
# string = input("Enter a string: ")
# substring = input("Enter a substring: ")
# occur1 = (string.find(substring)) + 1
# slice1 = string[occur1:]
# occur2 = (slice1.find(substring)) + (occur1)
# if occur2 == (occur1-1): 
#     print("The substring does not occur twice in the string.")
# else: 
#     print("The second occurrence of the substring is at index",occur2)