def numberSorter(arr):
  n = len(arr)
  sortedArr = []

  for i in arr:
    sortedArr.append(arr[0])
    if i in sortedArr > i:
      sortedArr.insert(i)
      continue
  return sortedArr
   


print(numberSorter([1,4,6,7,2]))


  


        