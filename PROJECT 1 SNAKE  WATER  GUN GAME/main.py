import random
import numpy as np
win=0
lose=0
draw=0
process=True
arr=np.array([['D','W','L'],['L','D','W'],['W','L','D']])
while process:
  user=int(input("enter 0 for snake, 1 for water ,2 for gun"))
  computer=random.randint(0,2)
 
  if arr[user,computer]=='W':
      win=win+1
      print("you won")
  elif  arr[user,computer]=='L':
      lose=lose+1   
      print("you lose")
  else:
      draw=draw+1
      print("you draw")
  y=input("do you  want to continoue(yes/no):")
  if y.lower()=='no':
      process=False        


print(f"number of times won={win}")
print(f"number of times lose={lose}")
print(f"number of times draw={draw}")