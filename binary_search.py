def binary_search_helper(arr, val, low, high):
    if low > high:
        return "NO Match"

    mid = low + (high - low) // 2

    if arr[mid] == val:
        return mid
    elif val > arr[mid]:
        return binary_search_helper(arr, val, mid+1, high)
    else:
        return binary_search_helper(arr, val, low, mid-1)


# def binary_search(arr, val):
#    return binary_search_helper(arr, val, 0, len(arr)-1)

arr = [2, 3, 4, 10, 40]
val = 10

result = binary_search_helper(arr, val, 0, len(arr)-1)

print("Index is", result)
