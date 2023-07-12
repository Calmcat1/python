def double_char(s):
    n = len(s)
    output = ""
    for i in range(n):
        for j in range(2):
            output += s[i]
    return output



print(double_char("here"))