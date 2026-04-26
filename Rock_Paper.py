import random

def get_computer_choice():
    return random.choice(["stone", "paper", "scissors"])


def decide_winner(user, computer):
    if user == computer:
        return "draw"
    elif (user == "stone" and computer == "scissors") or \
         (user == "paper" and computer == "stone") or \
         (user == "scissors" and computer == "paper"):
        return "win"
    else:
        return "lose"


def play_game():
    print("🎮 Welcome to Stone–Paper–Scissors!")
    
    while True:
        user_choice = input("\nEnter stone, paper, or scissors (or 'exit' to quit): ").lower()
        
        if user_choice == "exit":
            print("👋 Thanks for playing!")
            break
        
        if user_choice not in ["stone", "paper", "scissors"]:
            print("❌ Invalid choice! Try again.")
            continue
        
        computer_choice = get_computer_choice()
        print(f"🤖 Computer chose: {computer_choice}")
        
        result = decide_winner(user_choice, computer_choice)
        
        if result == "draw":
            print("🤝 It's a draw!")
        elif result == "win":
            print("🎉 You win!")
        else:
            print("😢 You lose!")


# Run the game
play_game()