# Restaurant Bill Discount Calculator

bill_amount = float(input("Enter your total bill amount: "))

if bill_amount >= 1000:
    discount = bill_amount * 0.20
    final_bill = bill_amount - discount
    print("You got 20% discount")
elif bill_amount >= 500:
    discount = bill_amount * 0.10
    final_bill = bill_amount - discount
    print("You got 10% discount")
else:
    discount = 0
    final_bill = bill_amount
    print("No discount available")

print("Discount:", discount)
print("Final bill amount:", final_bill)