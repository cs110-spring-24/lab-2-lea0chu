import random

while True:
  num = random.randint(0, 100)
  guess = 0
  wins = 0
  low = 0
  high = 0

  while guess != num:
    guess = int(input("Guess a number from 0 to 100: \n"))
    if guess == num:
      print("You won!")
      wins += 1
      print(f"It took you {high+low} guesses to solve it!")
    elif guess > num:
      print("Try a lower number!")
      low += 1
    else:
      print("Try a higher number!")
      high += 1

  restart = input("Run again? ")
  if "Yes" in restart:
    continue
  else:
    print("Goodbye.")
    break
