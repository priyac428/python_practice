# Topic : for loop with range
students = ["Anand", "Geetha", "Kumar"]
marks = [85, 90, 78]
dict = {}
for i in range(len(students)):
    dict[students[i]] = marks[i]
print(dict)