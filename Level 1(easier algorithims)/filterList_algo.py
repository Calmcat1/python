def filter_list(l):
    intList = []
    for char in l:
        if char != str(char):
            intList.append(char)
    return intList


print(filter_list([1,2,"3",4,"l"]))

#filters string from lists
        
            
           
        


