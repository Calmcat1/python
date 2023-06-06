def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            returnStr = i
    return returnStr
       
       
        

print(stray([1,1,1,2,1,1]))


#this finds the stray digit in the array, stray -> meaning the one that isnt alike to the rest