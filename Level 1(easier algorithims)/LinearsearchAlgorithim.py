def searchFunction(elmnt,arr):
    n = len(arr)
    for i in range(n):
        if elmnt == arr[i]:
            return f"element found at index {i}"
        elif elmnt not in arr:
            return "element not found"
        
     
print(searchFunction(4,[1,2,3,4]))


#recursion variant --

def searchRecursionFunction(elmnt,arr,i=0):
    n = len(arr)
    if i < n:
      if arr[i] != elmnt:
          searchRecursionFunction(elmnt,arr,i+1)
      else:
          print(f"element found at {i}")
    else:
        print(f"element is not found in the array")


searchRecursionFunction(3,[1,2,4,3])
