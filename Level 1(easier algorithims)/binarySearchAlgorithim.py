import math


def searchFunction(elmnt,arr):
    n = len(arr)
    l = 0
    r = n - 1
    while l < r:
        mid = math.floor((l+r)/2)
        if elmnt == arr[mid]:
            return mid
        elif elmnt > arr[mid]:
            l = mid + 1
        elif elmnt == arr[mid]:
            r = mid - 1
    else:
        return "data is not present"
      

print(searchFunction(4,[1,2,3,4,5,8]))
  


