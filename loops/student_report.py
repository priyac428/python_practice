# Topic : Student Report System
students = [
    {"name": "Priya", "age": 20, "marks": [80, 85, 90]},
    {"name": "Rahul", "age": 21, "marks": [40, 45, 50]},
    {"name": "Anu", "age": 19, "marks": [70, 75, 80]}
]

results = set()

for student in students:
    name = student["name"]
    marks = student["marks"]
    
    total = sum(marks)
    avg = total / len(marks)
    
    if avg >= 75:
        result = "Distinction"
    elif avg >= 50:
        result = "Pass"
    else:
        result = "Fail"
    
    results.add((name, avg, result))

for r in results:
    print(r)