# implement a quicksort algorithm
import math

# a basic quicksort algorithm, but more space complexity, lists are created with each function call
def quicksortbasic(arr):
    if len(arr) < 2:
        return arr
    else:
        # pick middle index as pivot
        pivotIndex = math.floor(len(arr) / 2)  
        pivot = arr[pivotIndex]
        leftArray = [i for i in arr[1:] if i <= pivot]
        rightArray = [i for i in arr[1:] if i > pivot]
        return quicksortbasic(leftArray) + [pivot] + quicksortbasic(rightArray)


# uses a partition function to sort the elements in place
def quicksort(arr = [], low = 0, high = None):
    if high is None:
        high = len(arr) - 1
    # in place sorting
    if low < high:
        index = _partition(arr, low, high)
        # initially partition arr array
        print(f'index is {index}')
        print(f'low is {low} high is {high}')
        quicksort(arr, low, index - 1) # quicksort left side of array
        quicksort(arr, index + 1, high) # quicksort right side of array

def _swap(arr, i1, i2):
    # print(f'swapping {arr[i1]} and {arr[i2]}')
    tmp = arr[i1]
    arr[i1] = arr[i2]
    arr[i2] = tmp

def _partition(arr, low, high):
    pivot = arr[high] # set pivot as last element
    i = low - 1 # low index is less than array index
    for j in range(low, high):
        if (arr[j] < pivot):
            # element is less than pivot so should be moved to lef side of array
            i += 1
            _swap(arr, j, i)
    _swap(arr, i + 1, high) # swap pivot element with highest, non-swapped element
    return i + 1 # return new pivot