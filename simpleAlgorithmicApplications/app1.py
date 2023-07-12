#application that takes some text and returns that text in code format i.e.
"""takes in for example, 

this is a test and returns
1. this is a test

also highlights the keywords that are not in my simple dictionary for code
"""

dictionary_of_keywords = ["this","for","if","while","true","false","is"] #-> dictionary version 1


def keywordhighlighter(psuedoFiles):
  output = ""
  files = psuedoFiles.split(" ")
  for word in files:
      if word in dictionary_of_keywords:
            output += word + "*"*len(word) + " "
      else:
          output += word + " "
  return output
          

  

print(keywordhighlighter('this is a simple test to test the app data'))


#this can also be a 8kyu Kata question(author: calmCat1)

#question description

"""
given the array:
dictionary_of_keywords = ["this","for","if","while","true","false","is"]

write down a code to format the words found in a sentense that are in this array
to be shown as below:

i.e. 
this -> ***this***
for -> ***for***

happy coding!

"""