# Topic : second largest element

arr = [10, 5, 20, 8, 20]

large =arr[0]
second_large =arr[0]

for i in arr:
    if i > large:
        second_large = large
        large = i
    elif i > second_large and i != large:
        second_large = i

print(second_large)