# Topic : Membership Operator
a=input("enter your message: ")
print("a"in a)
print("python" not in a)

# list of registered students
students = ["Rahul", "Priya", "Amit", "Sneha"]

# user trying to login
name = input("Enter your name ")

# check membership
if name in students:
    print("Login Successful!")
else:
    print("Access Denied!")

# checking not in
blocked_users = ["Amit"]

if name not in blocked_users:
    print("You are allowed to continue")
else:
    print("You are blocked")