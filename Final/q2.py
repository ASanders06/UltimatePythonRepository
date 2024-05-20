amount = 0
coin = ""
much = 50
change = 0
while amount < 50: 
    print("Amount due: ", much)
    coin = int(input("Insert coin: "))
    if coin == 50 or 25 or 5: 
        amount += coin
        much = 50 - amount
    else: 
        print("Error, coin type not accepted.")
if much < 0: 
    change = -(much)
    print("Change owed: ",change)
else: 
    change = 0
    print("Change owed: ",change)