def numberSorter(arr):
  max = arr[0]
  sortedArr = []
  for i in arr:
    if max < i:
      max = i
      sortedArr.append(max)
      arr.remove(max)
      
  return sortedArr
         



print(numberSorter([200,4,150,3,20,18]))


        