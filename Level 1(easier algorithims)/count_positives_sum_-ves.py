def count_positives_sum_negatives(arr):
    posSum = 0
    negSum = 0
    ansArr = []
    for i in arr:
        if i > 0:
            posSum +=1
        elif i < 0:
            negSum += i
    if len(arr) > 0:
        ansArr.append(posSum)
        ansArr.append(negSum)
    else:
        ansArr.clear()
    return ansArr


print(count_positives_sum_negatives([]))

#counts positves, returns sum of count and sums up negatives to give and arrat with both sums