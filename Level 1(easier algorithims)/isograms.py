def is_isogram(string):
    capsStr = string.upper()
    values = []
    for char in capsStr:
        if capsStr.count(char) == 1:
            values.append(True)
        else:
            values.append(False)
    return True if False not in values else False
            
            



print(is_isogram("hi"))
    