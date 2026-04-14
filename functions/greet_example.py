# Topic : Greet Example
def greet():
    print("Hello!")
greet()


def greet_user(name):
    print(f"Hello {name}!")
greet_user("priya")

def greet1(name="Friend"):
    print("Hello", name)

greet1()          # default
greet1("Priya")   # custom
