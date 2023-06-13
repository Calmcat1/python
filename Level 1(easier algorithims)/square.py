def is_square(n):
    return True if n**(1/2) == int(abs(n**(1/2))) else False


print(is_square(-1))