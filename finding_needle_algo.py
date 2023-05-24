
def find_needle(haystack):
  resultString = ""
  for i in haystack:
    if i == "needle":
      resultString = "needle has been found!"
    else:
      resultString = "needle has not been found"
  return resultString
    
    

print(find_needle([2,4,6,7,"needle"]))

array = []


#finds needle in array
