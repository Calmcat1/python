def bouncing_ball(h, bounce, window):
  counter = 1
  windowF = float(window)
  bounceF = float(bounce)

  if bounceF < 1 and h > 0:
    while h > windowF:
      h = h * bounceF
      counter += 1
      print(h)
  else:
    return -1 
  return counter
    
      
print(bouncing_ball(3,0.66,1.5))