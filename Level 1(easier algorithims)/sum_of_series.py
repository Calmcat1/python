
def series_sum(n):
    sum = 0
    deno = -2
    onedigit = 0
    for i in range(n):
          deno += 3
          sum += 1/deno
          if n < 0:
            onedigit = 1
    return str("{:.2f}".format(sum + onedigit))
       
       


print(series_sum(2))
     