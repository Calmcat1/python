def maximum_number(arr):
    maximum = arr[0]
    for i in arr:
      if maximum < i:
         maximum = i
    print(maximum)

def minimum_number(arr):
    minimum = arr[0]
    for i in arr:
      if minimum > i:
         minimum = i
    print(minimum)


        
  

arr1= [1,2,3,4,5,0.5,2]
maximum_number(arr1)
minimum_number(arr1)


#gets maximum and minimum in an array
        
