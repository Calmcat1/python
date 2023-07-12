def series_num(n):
    sum = 1
    series = 0
    oneDigit = 0
    for i in range(n-1):
          sum +=3 
          series += 1/sum 
    return series + oneDigit


print(series_num(2))
        