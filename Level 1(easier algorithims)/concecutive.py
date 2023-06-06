def first_non_consecutive(arr):
    n = len(arr)
    non_consec = 0
    for i in range(n):
      if arr[i] - arr[i-1] != 1:
          non_consec = arr[i]
      else:
          non_consec = None
    return non_consec




print(first_non_consecutive([1,2,3,6,7,8,10]))



            
