def tower_builder(n_floors):
    tower_arr = []
    output = " "
    for i in range(1,n_floors,2):
        output += "x"
        tower_arr.append(output)
        
    return tower_arr
      
#this was made using the python form of only multiplying the string "x"
print(tower_builder())

#this code rn is unfinished, needs a rework;