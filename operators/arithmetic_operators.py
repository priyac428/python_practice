# Topic : Arithmetic Operators
a = 10
b = 3
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  #Division 
print(a // b)  # Floor Division
print(a % b)  # Modulus
print(a ** b)  # Exponentiation

# price of one item
price = 50  

# quantity purchased
quantity = 4  

# total cost before discount
total = price * quantity
print("Total before discount:", total)

# discount (10%)
discount = total * 10 / 100
after_discount = total - discount
print("After discount:", after_discount)

# GST (5%)
gst = after_discount * 5 / 100
final_amount = after_discount + gst
print("Final amount to pay:", final_amount)