f_name = (input("First name: "))
l_name = str(input("Last name: "))
gpa = float(input("GPA: "))
days = ""
money = 0
if ("a" or "b" or "c" or "d" or "e" or "f" or "g" or "h" or "i" or "j" or "k") in l_name[0] == True: 
    days = "Monday and Thursday"
else: 
    days = "Tuesday and Friday"

if gpa >= 3.25: 
    money = 4000
    if gpa >= 3.49: 
        money = 8000
        if gpa >= 3.69: 
            money = 12000
            if gpa >= 3.85: 
                money = 16000
print("Hello,", f_name,". You should report to school on", days,". You are eligible for a scholarship of $",money,".")
