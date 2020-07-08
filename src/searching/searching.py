def linear_search(arr, target):
    # Your code here
    index = 0
    for i in arr:
        if i == target:
            return index
        else:
            index += 1

    return -1   # not found

# Write an iterative implementation of Binary Search


def binary_search(arr, target):
    # Your code here
    high = len(arr) - 1
    low = 0
    while low <= high:
        middle = (high + low) // 2
        if arr[middle] == target:
            return middle
        else:
            if arr[middle] > target:
                high = middle - 1
            elif arr[middle] < target:
                low = middle + 1

    return -1  # not found
