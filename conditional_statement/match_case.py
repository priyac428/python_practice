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




