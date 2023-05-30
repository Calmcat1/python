def likes(names):
  n = len(names)
  output = ""
  if n == 0:
    return "no-one likes this"
  elif n == 1:
    return output + names[0] + "likes this"
  elif n <= 2:
    return output + names[0] + " and " + names[1] + " like this"    
  elif n == 3:
    return output + names[0] + "," + names[1] + " and " + names[2] + " like this"
  elif n > 3:
    return output + names[0] + "," + names[1] + f" and {n-2} others like this"



print(likes(["hi","1","2","3","10"]))

    