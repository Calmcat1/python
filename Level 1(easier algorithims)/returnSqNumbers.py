def square_digits(num):
    output = ""
    for charNum in str(num):
        output += str(int(charNum) ** (2))
    return int(output)



print(square_digits(1234))