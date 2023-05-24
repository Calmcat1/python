
output = ""

answerlist = []


def count_sheep(n):
  for answer in range(n+1):
    if answer != n:
      answerlist.append(f"{answer} sheep...")
    else: 
       return answerlist
  
print(count_sheep(10))