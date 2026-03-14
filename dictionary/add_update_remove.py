 # Topic :  Add,Remove,Update Operations
a = {"name" : "priya",
     "age"  :  20,
     "education" : "engineering"}
print(a)

a["DOB"] = "1-1-2005" #adding element
print(a)

a["education"] = "computer science engineering" #updating element
print(a)

print(a.pop("DOB")) #Removes the specified key and returns the associated value.
del a["education"]  #Removes the specified key
print(a)

a.clear()
print(a) #empties the dictionary