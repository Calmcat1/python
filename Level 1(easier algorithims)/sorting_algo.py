def sortArr(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j] > arr[j+1]:
               arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


print(sortArr([2,5,7,10,18,-1,-4,-5]))

#this algorithim sorts the array in ascending order, using the bubble sort technique


    
