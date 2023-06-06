def largest_2_smallest(arr):
    newArr = []
    for num in arr:
        if num > num in newArr:
            continue
        else:
            newArr.append(num)
    return newArr
      


arr1 = [2,3,4,7,6,9,10,11,20,18,19,24]

print(largest_2_smallest(arr1))