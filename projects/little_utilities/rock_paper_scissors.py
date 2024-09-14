import random

options = ("rock", "paper", "scissors")
playing = True

while playing:
    computer_choice = random.choice(options)
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
    
    if user_choice not in options:
        continue
    
    print(f"Computer chose: {computer_choice}")
    
    if user_choice == computer_choice:
        print("It's a tie!")
    elif ((user_choice == "rock" and computer_choice == "scissors") or 
          (user_choice == "paper" and computer_choice == "rock") or
          (user_choice == "scissors" and computer_choice == "paper")): 
        print("You win!")
    else:
        print("You lose!")

    if input("Wanna play again? (y/n): ").lower() == "n":
        playing = False

print("Thanks for playing!")