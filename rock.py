import random

def play_again():
  """Asks the user if they want to play again.

  Returns:
      bool: True if the user wants to play again, False otherwise.
  """
  while True:
    answer = input("Do you want to play again? (y/n): ").lower()
    if answer in ("y", "n"):
      return answer == "y"
    else:
      print("Invalid input. Please enter 'y' or 'n'.")

def determine_winner(user_choice, computer_choice):
  """Determines the winner of the round.

  Args:
      user_choice: The user's choice (rock, paper, or scissors).
      computer_choice: The computer's choice (rock, paper, or scissors).

  Returns:
      str: "Win", "Lose", or "Tie" depending on the winner.
  """
  choices = ["rock", "paper", "scissors"]
  if user_choice == computer_choice:
    return "Tie"
  elif (choices.index(user_choice) + 1) % 3 == choices.index(computer_choice):
    return "Win"
  else:
    return "Lose"

def main():
  """The main function of the game."""
  user_score = 0
  computer_score = 0

  while True:
    print("\nRock Paper Scissors!")
    print(f"User Score: {user_score}, Computer Score: {computer_score}")

    user_choice = input("Choose rock, paper, or scissors: ").lower()
    valid_choices = ["rock", "paper", "scissors"]

    while user_choice not in valid_choices:
      user_choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()

    computer_choice = random.choice(valid_choices)

    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)

    if result == "Win":
      print("You win!")
      user_score += 1
    elif result == "Lose":
      print("You lose!")
      computer_score += 1
    else:
      print("It's a tie!")

    if not play_again():
      break

  print("\nThanks for playing!")

if __name__ == "__main__":
  main()
