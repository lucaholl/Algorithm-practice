# selection sort

def selectionsort(arr):
    outputArray = []
    outputLength = len(arr)
    # find smallest element in array and add it to output array
    while(len(outputArray) < outputLength):
        outputArray.append(arr.pop(_smallestelem(arr)))
    return outputArray

def _smallestelem(arr):
    smallestElement = arr[0]
    smallestIndex = 0
    for i in range(1, len(arr)):
        if (arr[i] < smallestElement):
            smallestElement = arr[i]
            smallestIndex = i
    return smallestIndex