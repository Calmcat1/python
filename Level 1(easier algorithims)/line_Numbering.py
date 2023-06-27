def number(lines):
    returnList = []
    for i in range(1,len(lines)+1):
        returnList.append(f"{i}:{lines[i-1]}")
    return returnList

print(number(['a','b','c']))