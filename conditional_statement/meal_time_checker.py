# Topic :  Meal Time Checker
time = int(input("Enter time in 24-hour format: "))

if time == 8:
    print("It's breakfast time.")
elif time == 13:
    print("It's lunch time.")
elif time == 20:
    print("It's dinner time.")
else:
    print("It's not meal time.")
