def tower_builder(n_floors):
    tower_builder_arr = []
    output = ""
    n_floors += n_floors
    for i in range(n_floors + 1):
        if i%2 != 0:
            print(i)
            output = " " * int((n_floors-i)/2) + "*" * i + " " * int((n_floors-i)/2)
            tower_builder_arr.append(output)
    return tower_builder_arr


print(tower_builder(3))
