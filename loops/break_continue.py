# Topic : Break Continue
for i in range(1,10):
    if i == 5:
        break
    print(i)
print("End")

for i in range(1,10):
    if i % 2 != 0:
        continue
    print(i)
print("End")

i=0
while i <= 10:
    if i == 5:
        break
    print(i)
    i += 1
print("End")

i=0
while i <= 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i)
print("End")

for i in range(1, 11):
    
    if i == 5:
        continue   # skip 5
    
    if i == 8:
        break      # stop loop at 8
    
    print(i)

    