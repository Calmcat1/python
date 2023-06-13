def accum(s):
    output = ""
    counter = 0
    for i in s:
        counter += 1
        output += str.capitalize(i * counter + "-")
    return output[0:-1]



print(accum("abcde"))