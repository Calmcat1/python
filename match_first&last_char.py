def feast(beast, dish):
    lenpar1 = len(beast)
    lenpar2 = len(dish)
    if beast[0:-(lenpar1-1)] == dish[0:-(lenpar2-1)] and beast[lenpar1-1:lenpar1] == dish[lenpar2-1:lenpar2]:
        return "true"
    else: return "false"



print(feast("chickandee","chocolate"))


#this algorithim compares the first and last characters of beast and dish and determines wheter they are the ame