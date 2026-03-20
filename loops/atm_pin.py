# Topic : ATM Pin Example
pin = 1234
trial = 1
while trial <= 3:
    user_pin = int(input("enter the pin:"))
    if user_pin == pin:
        print("correct")
        break
    else:
        print("Incorrect")
    trial +=1