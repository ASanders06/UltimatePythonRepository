exp = input("Expression? ") # 6-2
int1 = int(exp[0])
sign = exp[1]
int2 = int(exp[2])

if sign == "+": 
    eq_ans = int1 + int2
    print(int1,"+",int2,"=",eq_ans)
if sign == "-": 
    eq_ans = int1 + int2
    print(int1,"-",int2,"=",eq_ans)
if sign == "*": 
    eq_ans = int1 * int2
    print(int1,"*",int2,"=",eq_ans)
if sign == "/": 
    eq_ans = int1 / int2
    print(int1,"/",int2,"=",eq_ans)