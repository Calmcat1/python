def is_palindrome(s):
    n = len(s) - 1
    stringifiedS = str(s).lower()
    
    for i in range(n):
        if i == 1:
            return True
        else:
          if stringifiedS[i] == stringifiedS[n-i]:
              return True
          else: return False
    
    


is_palindrome("mada")
