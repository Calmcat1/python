def remove_smallest(numbers):
  min = numbers[0]
  n = len(numbers)
  for i in range(1,n):
    if min > i: 
      min = i
  return numbers.remove(1)
      
      


print(remove_smallest([1,2,3,4,5]))

