# Topic : Recursion
def fact(n):
    if n == 1:
        return 1
    else :
        return n * fact(n-1)
print(fact(9))

def sum(n):
    if n == 1:
        return 1
    else :
        return n + sum(n-1)
print(sum(5))