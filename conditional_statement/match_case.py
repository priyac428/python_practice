# Topic : Match Case
operator = input("enter the operator(+,-.*,/)")
a = int(input("enter the value of first number"))
b = int(input("enter the value of second number"))
match operator :
    case "+" :
        print(f"{a+b}")
    case "-" :
        print(f"{a-b}")
    case "*" :
        print(f"{a*b}")
    case "/" :
        print(f"{a/b}")

def whichWeekDay(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case 4:
            print("Thursday")
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _ :
            print("Invalid")
whichWeekDay(8)


                




