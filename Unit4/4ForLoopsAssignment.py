# ========== 4.4.1 ==========
# str = input("Type in a string: ")
# for letter in str: 
#     print(letter)
#     print("*")

# # ========== 4.4.2 ==========
# int = int(input("Type in an integer (pos): "))
# int2 = (-1*int)
# zero = 0
# for i in range(int2, 0):
#     print(i)
# for i in range(1, (int+1)):
#     print(i) 

# ========== 4.4.3 ==========
# list = []
# def list_of_stars(list): 
#     for items in list: 
#         print("*" * items)
# list_of_stars([1, 5, 3, 4])


# ========== 4.4.4 ========== 

# def palindromes(str): 
#     list = []
#     list2 = []
#     split = int(len(str)/2)
#     max = split
#     true = "True"
#     for index in range(len(str)):
#         if len(str) % 2 == 0: 
#             if index < split:
#                 list.append(str[index])
#             if index >= split:
#                 list2.append(str[index])
#         else: 
#             if index < split:
#                 list.append(str[index])
#             if index > split:
#                 list2.append(str[index])
  
#     is_palindrome = True
#     for letters in list: 
#         if letters != list2[max-1]: 

#             print("False")
#             is_palindrome = False
#             break
#         max -= 1
    
#     if is_palindrome:
#         print("True")
    
# palindromes("neveroddoreven")

# ========== 4.4.5 ==========
# list = []
# def sum_of_positives(list): 
#     numb2 = 0
#     for numb in list: 
#         if numb >= 0:
#             numb2 += numb
#         else: 
#             ()
#     print(numb2)
# sum_of_positives([1,2,3,-5])


# ========== 4.4.6 ==========
# list = []
# list2 = []
# def even_numbers(list): 
#     for numb in list: 
#         if numb % 2 == 0: 
#             list2.append(numb)
#     print(list2)
# even_numbers([2,4,5,8,7])

# ========== 4.4.7 ==========
# list = []
# list2 = []
# list3 = []
# numb2 = 0

# def list_sum(list, list2): 
#     which = 0
#     for numb in list: 
#         numb2 = numb + (list2[which])
#         list3.append(numb2)
#         which = which + 1
#         numb2 = 0
#     print(list3)
# list_sum([1, 2, 3], [3, 2, 1])

# ========== 4.4.8 ==========
# list = []
# def length_of_longest(list): 
#     longest = ""
#     for word in list:
#         if len(word) > len(longest): 
#             longest = word
#     print(longest)

# length_of_longest(["mark", "dorothy", "tim"])

# ========== 4.4.9 ==========
# list = []
# def shortest(list):
#     shortest = list[0]
#     for word in list:
#         if len(word) < len(shortest): 
#             shortest = word
#     print(shortest)
# shortest (["mark", "dorothy", "tim"])

