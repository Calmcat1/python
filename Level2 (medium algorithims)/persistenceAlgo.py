def persistence(n, counter=0):
  output = 1
  result = 0
  for charNum in str(n):
    output *= int(charNum)
    if output < 10:
      result = output
    else:
      counter += 1
      result = persistence(output)
  return counter
    
# this function returns multiplication to the ones place value, if the multiplication is greater than
# the ones place value, we run the result through recursion till we get the output in the
# ones place value



print(persistence(39))
   
  
