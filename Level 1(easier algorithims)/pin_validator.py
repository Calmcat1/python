def validate_pin(pin):
  chars = ['1','2','3','4','5','6','7','8','9']
  for char in pin:
    if char in chars and len(pin) == 6 or len(pin) == 4:
      returnStr = True
    else:
      returnStr = False
  return returnStr
   