def expanded_form(num):
    n = len(str(num))
    separation = 0
    for i in range(n):
        separation = str(10 **(n-1))
        separation2 = str(10 **(n-2))

    return separation


print(expanded_form(21000))
        