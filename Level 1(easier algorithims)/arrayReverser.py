def digitize(n):
  stringN = str(n)
  newList = []
  for i in reversed(stringN):
    newList.append(int(i))
  return newList
    


print(digitize([1,2,3,4,5]))