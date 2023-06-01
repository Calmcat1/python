def min_max(lst):
    max = lst[0]
    min = lst[0]
    newList = []
    for i in lst:
        if max < i:
            max = i
        if min > i:
            min = i
    newList.append(min)
    newList.append(max)
    return newList


print(min_max([1,2,3,4,5,6,7,8,9]))
  
    
        