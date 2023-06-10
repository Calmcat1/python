def is_pangram(s):
  stringifiedS = str(s)
  compareArray = []

  for char in stringifiedS:
    compareArray.append(char)

  alphaArr = ['a','b','c','d','e','f','g','h','i','j','k','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
  
  if compareArray := alphaArr:
    returnStr = True
  else:
    returnStr = False

  return returnStr



print(is_pangram("s"))
 