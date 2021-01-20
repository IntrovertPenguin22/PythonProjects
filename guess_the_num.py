#generating the random number
import random
guesses = 5
score = 0
while guesses > 0 and score < 20:
    main_num = random.randint(0,10)
    inp_num = input("Guess the number between 0 to 10: ")
    if main_num == inp_num:
      guesses -= 1
      score += 10
      print(f"You guessed it correctly! Your score is {score}")
    else:
      guesses -= 1
      score -= 5
      print(f"You guessed it wrong! Your score is {score}")
    if guesses == 0:
      print(f"You loose the the game! Your score is {score}")
    elif score == 20:
      print(f"You won the game! Your score is {score}")
