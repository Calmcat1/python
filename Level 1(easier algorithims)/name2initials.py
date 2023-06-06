def initializer(name):
  stringify = str(name)
  stringArray = stringify.split(" ")
  output = ""
  for string in stringArray:
    output += (string[0: -(len(string)-1)]) + "."
  return output.strip('.')

    
    

    


print(initializer("Lee Gitonga"))


# function returns initials of the names it is fed with (2)