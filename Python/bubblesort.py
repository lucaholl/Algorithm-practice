# bubble sort module

def bubbleSort(arr):
    swaps = 1

    while(swaps > 0):
        swaps = 0
        for i in range(0, len(arr) - 1):
            if arr[i]  > arr[i+1]:
                tmp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = tmp
                swaps +=1
    
    return arr
