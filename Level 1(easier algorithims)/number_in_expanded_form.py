def expanded_form(num):
    stringifiedNum = str(num)
    n = len(stringifiedNum)
    output = ""
    decrementCounter = 0
    for i in stringifiedNum:
        decrementCounter += 1
        output += str(int(i) * (10 ** (n-decrementCounter))) + " + "
        
        

    return output[0: len(output)-2]


print(expanded_form(123456))


#function takes in a number and returns it as a separated value(addition of its place values)
        