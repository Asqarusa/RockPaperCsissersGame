import random

user_win = 0
computer_win = 0

options = ["rock", "paper", "scissors"]
while True:
    user_input =input("Type Rock/Paper/Scissors or Q to quit: ").lower()
    if user_input == "q":
       break

    if user_input not in options: #list
        continue
    random_num = random.randint(0, 2)
    #Rock = 0 P = 1 S = 2
    computer_pick = options[random_num]
    print("Computer Pciked", computer_pick, "." )

    if user_input == "rock"and computer_pick == "scissors":
        print("you won!")
        user_win += 1
        
    elif user_input == "paper"and computer_pick == "rock":
        print("you won!")
        user_win += 1
        
    elif user_input == "scissors"and computer_pick == "paper":
        print("you won!")
        user_win += 1
    else:
        print("You Lost!")   
        computer_win += 1

print("You got", user_win , "times and Computer win", computer_win, "times.")
print("Thanks, Bye")