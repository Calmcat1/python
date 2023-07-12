def century(year):
    counter = 0
    for i in range(0, year, 100):
        counter += 1
    return counter
    
print(century(1601))