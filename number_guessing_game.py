import random

def start_game():
    computer_number = random.randint(0, 100)
    guess = -1 
    wins = 0
    low = 0
    high = 0
    while guess != computer_number:
        guess = int(input("Guess a number from 0 to 100: \n"))
        if guess == computer_number:
            print("You won!")
            wins += 1
            print(f"It took you {high+low} guesses to solve it!")
        elif guess > computer_number:
            print("Try a lower number!")
            low += 1
        else:
            print("Try a higher number!")
            high +=1
while True:
    restart = input ("Run again? ")
    if "Yes"in restart:
      start_game()
    else:
      print("Goodbye.")
      break


