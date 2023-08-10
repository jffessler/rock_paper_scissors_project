import random
import time

computer_wins = 0
human_wins = 0

def playerSelection():
    player_choice = "empty"
    #player chooses their position or whether they would like to play
    while True:
        player_choice = input("Select your move: Rock/Paper/Scissors or Q to quit: ")
        if player_choice.lower() == 'q':
            return print("Thank you for playing!")
        elif player_choice.lower() != "rock" and player_choice.lower() != "paper" and player_choice.lower() != "scissors":
            print("Incorrect input!")
        else:
            print("Good Luck!")
            return player_choice.lower()

def rpsCountdown(choice):
    moves = {"rock": 0,"paper": 1,"scissors": 3}
    print("One the count of three and shoot!")
    time.sleep(0.5)
    print("1")
    time.sleep(0.5)
    print("2")
    time.sleep(0.5)
    print("3")
    t1 = time.time()
    input("Shoot! ...")
    t2 = time.time()
    diff = abs(t1 - t2)
    print(diff)
    print(choice)
    if diff < 0.25:
        #computer has advantage to tie or win
        print("You are early")
    elif diff > 0.25 and diff < 0.75:
        #random chance for both players
        print("Fair game!")
    else:
        #player has advantage to tie or win
        print("Cheater! You looked!")

choice = playerSelection()
rpsCountdown(choice)
