def postiveSum(arr):
    posSum = 0
    sumArray = []
    for num in arr:
        if num > 0:
            sumArray.append(num)
        else:
            posSum = 0
    for i in sumArray:
        posSum += i
    return posSum

            
arr1 = [1,-2,3,4,5]
print(postiveSum(arr1))