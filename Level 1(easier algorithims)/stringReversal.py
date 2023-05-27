
def reverse_words(text):

  output = ""
  strArray = str.split(text," ")


  for word in strArray:
      for char in reversed(word+" "):
         output += char 
  return output.strip()



      
      


print(reverse_words("hey this is one and 2"))
    
