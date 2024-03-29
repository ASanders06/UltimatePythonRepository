print("########## 1.3.1 ##########")

name = "Tim Tester"
age = 20
skill1 = "python"
level1 = "beginner"
skill2 = "java"
level2 = "veteran"
skill3 = "programming"
level3 = "semiprofessional"
lower = 2000
upper = 3000

print("my name is "+ name+", I am",age,"years old" + "\n")
print("my skills are")
print("- ",skill1, "("+level1 +")")
print("- ",skill2, "("+level2+")")
print("- ",skill3, "("+level3+")" + "\n")
print(f"I am looking for a job with a salary of {lower}-{upper} dollars per month")


print("########## 1.3.2 ##########")
x = 27
y = 15
ans1= str(x + y)
ans2= str(x - y)
ans3= str(x * y)
ans4= str(x / y)
print (x,"+", y, "=", ans1)
print (x,"-", y, "=", ans2)
print (x,"*", y, "=", ans3)
print (x,"/", y, "=", ans4)

x = 4
y = 9
ans1= str(x + y)
ans2= str(x - y)
ans3= str(x * y)
ans4= str(x / y)
print (x,"+", y, "=", ans1)
print (x,"-", y, "=", ans2)
print (x,"*", y, "=", ans3)
print (x,"/", y, "=", ans4)

print("########## 1.3.3 ##########")
print(5, end="")
print(" + ", end="")
print(8, end="")
print(" - ", end="")
print(4, end="")
print(" = ", end="")
print(5 + 8 - 4, end="")