# Topic : Variable Length Argument
# *args
def add(*num):
    return sum(num)
print(add(1,4,1))

def avg(*marks):
    return sum(marks)/len(marks)
print(avg(20,37,44))

# **kwargs
def student_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

student_info(name="Anand", age=22, course="Python")

 