def find_it(seq):
    for number in seq:
        if seq.count(number)%2 != 0:
            returnNumber = number
    return returnNumber
   
        


        



print(find_it([1,1,1,2,2,3,4,4,5,5,1,1,1]))




