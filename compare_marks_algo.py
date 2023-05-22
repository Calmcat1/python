
#this is similar to the len function
def arrayCounter(arr):
    counter = 0
    for i in arr:
        counter = counter + 1
    return counter




def better_than_average(classpoints, yourpoints): 
    sum = 0
    average = 0
    for points in classpoints:
        sum +=points
        average = sum/arrayCounter(classpoints)
        if yourpoints > average:
            boolean = True
        else:
            boolean = False
    print(average)
    return boolean
    

marksArr = [1,2,3,4,5]


yourPoints = 3


print(better_than_average(marksArr,yourPoints))