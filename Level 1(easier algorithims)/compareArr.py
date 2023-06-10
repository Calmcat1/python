def comp(array1, array2):
    n = len(array1)
    resultsArr = []
    returnStr = None
    for i in range(n):
      if array1[i] ** (2) == array2[i]:
          returnStr = True
      else:
          returnStr = False
      resultsArr.append(returnStr)
      if False in resultsArr:
          returnStr = False
    return returnStr, resultsArr


print(comp([5,10,15,20,25],[25,100,225,400,625]))
  
