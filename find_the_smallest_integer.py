def find_smallest_int(arr):
    min = arr[0]
    for num in arr:
        if min > num:
            min = num
    return min

arr = [1,2,3,4,5,6,10]

print(find_smallest_int(arr))

#finds smallest no in an array