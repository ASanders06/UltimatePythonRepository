# ========== 3.1.1 ==========
numb = 2
while numb <= 30:
    print(numb)
    numb += 2
print("Go!")

# ========== 3.1.2 ==========

print("Are you ready?")
number = int(input("Please type in a number: "))
while number > 0:
    print(number)
    number += -1
print("Go!")

# ========== 3.1.3 ========== *add an error msg for neg numbers if you have time
numb = int(input("Upper limit: "))
numb2 = 1
if numb < 0: 
    print("ERROR, NEGATIVE INTEGER.")
else: 
    while numb2 < numb: 
        print(numb2)
        numb2 += 1

# ========== 3.1.4 ==========
numb = float(input("Upper limit: "))
numb2 = 1
while numb2 < numb: 
    print(numb2)
    numb2 = numb2*2

# ========== 3.1.5 ==========
numb = int(input("Upper limit: "))
base = int(input("Base: "))
numb2 = 1
while numb2 < numb: 
    print(numb2)
    numb2 = numb2 * base

# ========== 3.1.6 ==========
limit = int(input("Limit: "))
addlist = 1
change = 2
while addlist < limit: 
    addlist+= change
    change+=1
print(addlist)
