def paperwork(n, m):
    if n < 0 or m < 0:
        returnval = 0
    else:
        returnval = n * m
    return returnval


print(paperwork(5,5))
