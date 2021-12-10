from array import array


def binary_search(array, target):
    left = 0
    right = len(array) - 1
    while left <= right:
        middle = (left + right) //2
        match = array[middle]
        if match == target:
            return middle
        elif target < match:
            right = middle - 1
        else:
            left = middle + 1
    return - 1

array = [1,3,5,6,7,8,9,10]
print(binary_search(array=array, target= 5))        