#algorithim

array = [10, 4, 3, 50, 23, 90]


def count(array):
    counter = 0
    for i in array:
        counter = counter + 1
    return counter


rangenum = int(count(array))


bigno = array[0]

for i in range(rangenum):
    if bigno > array[i]:
        bigno = array[i]
    print(bigno)
    

      




    
    







