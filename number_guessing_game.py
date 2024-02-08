
import random

num = random.randint(1, 100)
user = 0
wins = 0
high = 0
low = 0

while num != user:
  user = int(input("Enter your guess: "))  
  if user > num:
    print(f"Too high.")
    high += 1
  elif user < num:
    print(f"Too low.")
    low += 1
  else:
    print("You got it!")
    wins += 1
    print(f"It took you {high+low} guesses to solve it!")
    
again = input("Run again?: ")
while True:
  if 'Yes' in again:
    user = int(input("Enter your guess: "))
    if user > num:
      print(f"Too high.")
      high += 1
    elif user < num:
      print(f"Too low.")
      low += 1
    elif user == num:
      print("You got it!")
      wins += 1
      print(f"It took you {high+low} guesses to solve it!")
  else: 
    print("Goodbye")
    break
