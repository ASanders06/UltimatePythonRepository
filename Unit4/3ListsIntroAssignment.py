# ========== 4.3.1 ==========
# replace, don't add to the length of the list
list1 = [1,2,3,4,5]
ind = []
val = []
while ind != -1: 
    ind = int(input("Index: "))
    if ind != -1: 
        val = input("New value: ")
        list1[ind] = val
        print(list1)


# ========== 4.3.2 ==========
# list1 = []
# how = int(input("How many items? "))
# when = 1
# while when <= how: 
#     item = input("Item" + str(when) + ": ")
#     list1.append(item)
#     when += 1
# print(list1)

# ========== 4.3.3 ==========
# list1 = []
# which = 1
# arx = []
# while arx != "x": 
#     arx = input("Ad(d), (R)emove, or E(x)it: ")
#     if arx == "d": 
#         list1.append(which)
#         which+=1
#         print("The list is now: " + str(list1))
#     elif arx == "r": 
#         list1.pop((len(list1)-1))
#         if which == 1: 
#             which = 1
#         else: 
#             which -= 1
#             print("The list is now: " + str(list1))
# print("Bye bye!")

# ========== 4.3.4 ==========
# hi = 1
# list1 = []
# list2 = []
# word = []
# while hi == 1: 
#     word = input("Word: ")
#     list1.append(word)
#     if word in list2: 
#         break
#     if word in list1: 
#         list2.append(word)
    


# print("You typed in " + str((len(list1)-1)) + " words.")
