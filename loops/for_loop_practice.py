# Topic : for loop Practice
name = "priya"
for letter in name:
    print(letter*5)


for index,letter in enumerate(name):    #enumerate
    z = letter * (index + 1)             
    print(z)

a = [22,44,55,77,88]                
for index,num in enumerate(a):
    print(f"{num} in {index}th position")

