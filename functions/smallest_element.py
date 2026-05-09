# Topic : smallest element
arr = [10, 25, 5, 40, 15]

smallest = arr[0]

for i in arr:
    if i < smallest:
        smallest = i

print("Smallest element is:", smallest)