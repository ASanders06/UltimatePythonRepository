# ========== 3.4.1 ==========
# def seven_dwarves(one, two, three, four, five, six, seven): 
#     print(one+"\n"+two + "\n"+ three + "\n"+ four+ "\n"+five + "\n"+six + "\n"+seven)
# seven_dwarves("Bashful", "Doc", "Dopey", "Grumpy", "Happy", "Sleepy", "Sneezy")

# ========== 3.4.2 ==========
# letter1 = ""
# word = input("Type in a word: ")
# def first_character(letter1): 
#     letter1 = word[0:1]
#     print(letter1)
# first_character(word)
# ========== 3.4.3 ==========
# def mean(numb1, numb2, numb3): 
#     numb1 = (numb1 + numb2 + numb3) / 3
#     print(numb1)
# mean(1, 2, 3)

# ========== 3.4.4 ==========

# def print_many_times(text, times): 
#     print((text + "\n") * times)
# print_many_times("hi", 7)

# ========== 3.4.5 ==========
# def hash_square(length): 
#     hash = "#" * length
#     times = 1
#     while times <= length: 
#         print(hash)
#         times+=1
# hash_square(7)

# ========== 3.4.6 ==========

# def chessboard(numb): 
#     count = 1
#     while int(count) <= numb: 
#         if numb % 2 == 0: 
#             print("10" * int(numb/2))
#             count+=1
#             print("01" * int(numb/2))
#             count+=1
#         else: 
#             print("10" * int(numb/2) + "1")
#             count+=1
#             if count > numb: 
#                 break
#             print("01" * int(numb/2) + "0")
#             count+=1
#             if count > numb: 
#                 break
# chessboard(5)

