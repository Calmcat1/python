def binary_array_to_number(arr):
    n = len(arr)
    sum = 0

    for i in range(n):
       sum += arr[i] * (2**(n-(i+1)))
    return sum



print(binary_array_to_number([1,0,1]))


