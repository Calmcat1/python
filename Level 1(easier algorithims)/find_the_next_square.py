from math import sqrt

def find_next_square(sq):
    
    newNumber = sqrt(sq) + 1
    return newNumber ** (2) if newNumber == int(newNumber) else -1

print(find_next_square(5))