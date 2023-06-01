def is_valid_walk(walk):
    if len(walk) > 10 or len(walk) < 10:
        return False
    elif walk[0] != walk[len(walk)-1]:
        return False
    else:
        return True
    

#this is a code to determine whether the walk is valid or not
        
