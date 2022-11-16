import random

#while loop to keep playing game unless indicated
while True:

  print("Can you guess the magic number? Let's find out!")
  
  #computer choice
  numbers = ['1', '2', '3', '4', '5']
  comp_choice = random.choice(numbers)
  
  #player choice
  player_choice = input("Enter a number between 1 and 5. ")
  
  #validate player choice
  if player_choice not in (numbers):
    print("The number you entered is invalid. Please try again.")
    player_choice = input("Enter a number between 1 and 5. ")
    
  
  print(f"You chose {player_choice}, and the computer chose {comp_choice}.")
  
  #check winner
  if player_choice == comp_choice:
    print("Congratulations! You guessed the magic number!")
  else:
      print("You didn't guess the magic number. You lose.")
  
  play_again = input("Would you like to play again? Enter y or n. ")
  if play_again != 'y':
    print("Thanks for playing!")
    break
    