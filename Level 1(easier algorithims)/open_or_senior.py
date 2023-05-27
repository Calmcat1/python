def open_or_senior(data):
    returnArr = []
    for arr in data:
         if arr[0] >= 55 and arr[1] > 7:
              returnArr.append("Senior")
         else:
              returnArr.append("Open")
    return returnArr
              


print(open_or_senior([[55,12],[17,12]]))
              
            