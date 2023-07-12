
# unit case, checks whether the function returns 5, returns true if it does else false
def checkWhetherReturns5(function):
    if function == 5:
        print("True") 
    else:
        print("false")


# Testable case, this is the case that is being tested
def returnNumber(x):
    return x



#running the test in python
print(checkWhetherReturns5(returnNumber(5))) #-> returns True

print(checkWhetherReturns5(returnNumber(10))) #-> returns False
        

        


