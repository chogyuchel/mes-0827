import random
print("수정한부분")
def rsp_game():
    choices = ['rock', 'scissors', 'paper']
    user = input("Choose rock, scissors, or paper: ").lower()
    if user not in choices:
        print("Invalid choice.")
        return
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == 'rock' and computer == 'scissors') or \
         (user == 'scissors' and computer == 'paper') or \
         (user == 'paper' and computer == 'rock'):
        print("You win!")
    else:
        print("You lose!")

if __name__ == "__main__":
    rsp_game()
