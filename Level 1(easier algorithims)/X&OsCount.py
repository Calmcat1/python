def xo(s):
  captialStringArr = []
  for char in s:
    captialStringArr.append(char.capitalize())
  return True if captialStringArr.count("X") == captialStringArr.count("O") else False