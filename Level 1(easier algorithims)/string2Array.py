def string_to_array(s):
  output = ""
  for char in s:
    output += char
  return output.split(" ")



print(string_to_array("this is one"))