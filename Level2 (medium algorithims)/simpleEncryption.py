def encrypt(text, n):
    x = len(text)
    oddind = ""
    evenind = ""
    output = ""
    result = ""
    for i in range(n):
      for j in range(x):
          if j%2 !=0:
              oddind += text[i]
          else:
              evenind += text[i]
          output = oddind + evenind
      result = encrypt(output,i)
    return result
    



print(encrypt("hello",4))


    