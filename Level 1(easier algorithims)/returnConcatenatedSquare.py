def returnNumberSquares(numberstosq):
    output = ""
    for numbers in numberstosq:
        trueNumber = int(numbers) ** (2)
        strNumber = str(trueNumber)
        output += strNumber
    return output

  
print(returnNumberSquares("12345"))

        
    

