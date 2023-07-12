def longest(a1, a2):
    combinedChar = a1 + a2
    output = ""
    for char in combinedChar:
        if char in output:
            continue
        else:
            output += char
    return "".join(sorted(output))


print(longest("xxxxyyyyabklmopq","xyaabbbccccdefww"))
        


        