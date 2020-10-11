def binary_search(arr, val):
    low = 0
    high = len(arr)-1

    while (low <= high):

        mid = low + (high-low)//2

        if val == arr[mid]:
            return mid

        if val < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return "No match"


arr = [2, 3, 4, 10, 40]
val = 10

result = binary_search(arr, val)

print("index of the element is", result)
