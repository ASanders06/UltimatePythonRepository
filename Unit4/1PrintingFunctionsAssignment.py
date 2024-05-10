# # ========== 4.1.1 ==========
def line(integral, sting): 
    if sting == "": 
        print("*" * integral)
    else: 
        slice = sting[0:1]
        print(slice * integral)
line(7, "")

# ========== 4.1.2 ==========
# def box_of_hashes(numb): 
#     count = 1
#     while count <= numb: 
#      line(10, "#")
#      count +=1   
# box_of_hashes(5)

# # ========== 4.1.3 ==========
# # def square_of_hashes(numb): 
# #    count = 1
# #    while count <= numb: 
# #      line(numb, "#")
# #      count +=1   
# # square_of_hashes(5)

# # # ========== 4.1.4 ==========
# # def square(integral, sting): 
# #    count = 1
# #    while count <= integral: 
# #      line(integral, sting)
# #      count +=1
# # square(3, "hi")
   

# # ========== 4.1.5 ==========
# def triangle(numb): 
#    count = 1
#    while count <= numb: 
#       line(count, "#")
#       count +=1
# triangle(4)

# ========== 4.1.6 ==========
# def shape(numb1, key1, numb2, key2): 
#     count = 1
#     while count <= numb1: 
#       line(count, key1)
#       count +=1
#     count = 1
#     while count <= numb2: 
#         line(numb1, key2)
#         count +=1   
# shape (5, "X", 3, "*")

# ========== 4.1.7 ==========
def spruce(numb): 
    count = 1
    begi = int(numb)
    end = int(numb)
    print("A spruce!")
    while count <= (numb*2): 
        print((" " * begi) + ("*" * count) + (" " * end))
        count += 2
        begi -= 1
        end += 1
    begi = int(numb)
    end = int(numb)
    print((" " * begi) + ("*") + (" " * end))
spruce(9)