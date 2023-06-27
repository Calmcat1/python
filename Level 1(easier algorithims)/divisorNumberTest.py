def divisors(n):
    counter = 0
    ansArray = []
    for i in range(1,n+1):
        ans = n/i
        if ans == int(ans):
            counter = counter + 1
            ansArray.append(ans)
        else:
            continue
    return counter, ansArray


print(divisors(500000))
            
        