def get_count(sentense):
  counter = 0
  for char in sentense:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
      counter = counter + 1
  return counter
    


print(get_count("fshaiojkioksio"))


