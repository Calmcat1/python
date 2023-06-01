def sum_array(arr):
    min = arr[0]
    max = arr[0]
    sum = 0
    for num in arr:
        if max < num:
            max = num
        elif min > num:
            min = num
        sum += num
    return sum 


print(sum_array([1,2,3,4,5]))
    