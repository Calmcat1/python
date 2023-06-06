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

    #gets minimum and maximum in the list it is fed


        
  

arr1= [5,10,15,202,20]
maximum_number(arr1)
minimum_number(arr1)


#gets maximum and minimum in an array
        
