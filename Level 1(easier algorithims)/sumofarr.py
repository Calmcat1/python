def sum_array(a):
    sum = 0
    for num in a:
        if len(a) > 0:
          sum += num
        else:
           sum = 0
    return sum


print(sum_array([1,2,3,4,5]))