# # ========== 3.2.1 ==========
# str1 = input("Type in a string: ")
# str2 = int(input("Type in an amount: "))
# print(str1 * str2)

# ========== 3.2.2 ==========
# str1 = input("Type in string 1: ")
# str2 = input("Type in string 2: ")
# if len(str1) > len(str2): 
#     print(str1,"is longer.")
# elif len(str1) < len(str2): 
#     print(str2,"is longer.")
# else: 
#     print("The strings are equally long")

# ========== 3.2.3 ========== 
# str1 = input("Type in a string: ")
# leng = -1
# while leng > -(len(str1)): 
#     print(str1[leng])
#     leng = leng - 1
# print(str1[0])

# ========== 3.2.4 ==========
# str1 = input("Type in a string: ")
# if str1[1] == str1[-2]: 
#     print("The second and second to last characters are the same.")
# else: 
#     print("The second and second to last characters are different.")

# ========== 3.2.5 ==========
# width = int(input("Width: "))
# print ('#' * width)

# ========== 3.2.6 ==========
# width = int(input("Width: "))
# height = int(input("Height: "))
# when = 1
# while when <= height: 
#     print ('#' * width)
#     when += 1

# ========== 3.2.7 ==========
# str1 = "a"
# length = 0
# while len(str1) > 0: 
#     str1 = input("Type in a string: ")
#     length = len(str1)
#     print(str1)
#     print('-' * length)
#     if str1 == "": 
#         break

# ========== 3.2.8 ==========
# str1 = input("Type in a string: ")
# length = 20 - len(str1)
# print(("*" * length) + str1)

# ========== 3.2.9 ==========
# str1 = input("Word: ")
# if len(str1) % 2 == 0: 
#     mid = mid = int((len(str1) + 30) / 2)
#     mid = int(mid - (len(str1))-1)
#     print("*" * 30)
#     print("*" + (" " * mid) + str1 + (" " * (mid)) + "*")
#     print("*" * 30)
# else: 
#     mid = int(((len(str1) + 30) / 2)-len(str1))
#     print("*" * 30)
#     print("*" + (" " * mid) + str1 + (" " * (mid-1)) + "*")
#     print("*" * 30)
