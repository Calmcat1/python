def set_alarm(employed, vacation):
    if employed == True and vacation == False:
        return True
    elif employed == True and vacation == True:
        return False
    else:
        return False