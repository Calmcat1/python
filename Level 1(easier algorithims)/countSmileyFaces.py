def count_smileys(arr):
    allowedChars = [":)", ";)", ":-)", ":~)", ":D", ":-D", ":~D", ";-)", ";~)",";-D",";~D",";D" ]
    trueArray = []
    for char in arr:
        if char in allowedChars:
            trueArray.append(True)
        else:
            trueArray.append(False)
    return trueArray.count(True)
    

print(count_smileys([":)", ":-)", ":D"]))