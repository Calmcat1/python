def find_average(numbers):
    if len(numbers) > 0:
      sum = 0
      for number in numbers:
          sum += number
          average = sum/len(numbers)
      return average
    else:
       return 0



print(find_average([1,2,3,4,5,6]))