# Topic : Input And Output Functions
boy_name = input("enter boy name: ")
boy_age = int(input("enter boy age: "))

girl_name = input("enter girl name: ")
girl_age = int(input("enter girl age: "))

diff_age = abs(boy_age - girl_age)

print(boy_name+" weds "+girl_name+" age difference is "+str(diff_age))
print(boy_name,"weds",girl_name,"age difference is",diff_age)
print(f"{boy_name} weds {girl_name} age difference is {diff_age}")




