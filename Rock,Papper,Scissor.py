import random

class RockPaperScissors:
    def __init__(self):
        self.choices = ["rock", "paper", "scissors"]

    def get_computer_choice(self):
        return random.choice(self.choices)

    def determine_winner(self, player, computer):
        if player == computer:
            return "It's a tie!"
        elif (player == "rock" and computer == "scissors") or \
             (player == "paper" and computer == "rock") or \
             (player == "scissors" and computer == "paper"):
            return "You win! 🎉"
        else:
            return "Computer wins! 😢"

    def play(self):
        print("Welcome to Rock-Paper-Scissors!")
        
        while True:
            player_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ").lower()
            if player_choice == "quit":
                print("Thanks for playing! Goodbye. 👋")
                break
            if player_choice not in self.choices:
                print("Invalid choice! Please enter rock, paper, or scissors.")
                continue
            
            computer_choice = self.get_computer_choice()
            print(f"Computer chose: {computer_choice}")
            print(self.determine_winner(player_choice, computer_choice))


if __name__ == "__main__":
    game = RockPaperScissors()
    game.play()