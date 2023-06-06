def duplicate_encode(word):
    strArr = []
    output = ""
    for char in word:
        strArr.append(char)
        if strArr.count(char) > 1:
            returnChar = ")"
        else:
            returnChar = "("
        output += returnChar
    return output
    
        
    

        



print(duplicate_encode("this is one"))


#encodes characters to ) if duplicate else ()
    