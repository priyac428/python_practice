# Topic :  Dictionary methods
a = {"name" : "priya",
     "age"  :  20,
     "education" : "engineering"}
print(a.keys())
print(a.values())
print(a.items())
b = {"DOB" : "01-01-2005"}
a.update(b)
print(a)