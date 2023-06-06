def correct(s):
    replace_dict = {
       '0' : 'O',
       '1' : 'I',
       '5' : 'S'
    }
    for char in s:
        if char == "0" or char == '1' or char == '5':
          returnStr = s.replace(char,replace_dict[char])
    return returnStr
    

print(correct("L0ND0N"))
        



    