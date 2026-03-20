is_passed = True
i = 1
while is_passed:
    i=i+1  
    if i%2 != 0:              
        continue
    if i>100:
        break
    print(f"try {i}")
print("I gave up!")



i=1
while i <= 10:
    print("priya "*i)
    i=i+1

i=1
while i <= 10:
    x=1
    while x<=i:
        print("priya",end="")
        x=x+1
    print("")
    i=i+1


