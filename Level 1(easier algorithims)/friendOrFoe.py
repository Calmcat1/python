def friend(x):
    friends = []
    for string in x:
        if len(string) == 4:
            friends.append(string)
    return friends


print(friend(['leee','four','two','seven','five']))
            