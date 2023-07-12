def find_multiples(integer, limit):
    multipleArr = []
    for num in range(1,limit+1):
        if num%integer == 0:
            multipleArr.append(num)
    return multipleArr



print(find_multiples(2,6))

            