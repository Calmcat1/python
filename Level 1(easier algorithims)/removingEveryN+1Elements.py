def remove_every_other(my_list):
    n = len(my_list) 
    newList = []
    for i in range(0,n,2):
      newList.append(my_list[i])
    return newList
   


print(remove_every_other(["hello","remove","hello","remove"]))



