# Topic : List Comprehension
l = [1,2,3,4]
sl = [num**2 for num in l]
print(sl)


a = [b for b in range(1,11)]
c = [d for d in a if d % 2 == 0]
print(a)
print(c)

name = ["priya","keerthi"]
z = [n[1] for n in name]
print(z)