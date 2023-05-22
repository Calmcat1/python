def repeat_str(repeat, string):
    output = ""
    for i in range(repeat+1):
        output += string
    return output

print(repeat_str(5,"hello"))
        