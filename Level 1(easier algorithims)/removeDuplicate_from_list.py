def remove_duplicates(arr):
    nonDuplicateArr = []
    for number in arr:
        if number in nonDuplicateArr:
           continue
        else:
            nonDuplicateArr.append(number)
    return nonDuplicateArr

      
    

print(remove_duplicates([1,1,2,2,3,3,4,4]))


#takes numbers, checks whether they are in the duplicate array or not, if it is 
# it continues(skippes the appending process)