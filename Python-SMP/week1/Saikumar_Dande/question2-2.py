# Binary search method.
list1 = [1, 2, 3, 4, 5, 6]
search = 5
low = 0
high = len(list1)-1
while low <= high:
    middle = ((low+high)//2)
    if search == list1[middle]:
        print("Element is found")
        break
    elif search > list1[middle]:
        low = middle + 1
    elif search < list1[middle]:
        high = middle - 1
if low > high:
    print("Element not found")
