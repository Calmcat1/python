def unique_in_order(sequence):
    newArray = []
    for string in sequence:
        if string in newArray:
            continue
        else:
            newArray.append(string)
    return newArray