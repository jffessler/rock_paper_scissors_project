import random
import time

def playerSelection():
    player_choice = "empty"
    #player chooses their position or whether they would like to play
    while True:
        player_choice = input("Select your move: Rock/Paper/Scissors or Q to quit: ")
        if player_choice.lower() == 'q':
            print("Thank you for playing!")
            return player_choice.lower()
        elif player_choice.lower() != "rock" and player_choice.lower() != "paper" and player_choice.lower() != "scissors":
            print("Incorrect input!")
        else:
            print("Good Luck!")
            return player_choice.lower()

def rpsCountdown(choice):
    computer_wins = 0
    human_wins = 0
    computer_moves = ["rock","paper","scissors"]
    comp_mod_rock = ["rock","paper"]
    comp_mod_paper = ["scissors","paper"]
    comp_mod_scissors = ["rock","scissors"]

    while choice != 'q':
        #Count down for move reveal
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

        if diff < 0.25:
            #computer has advantage to tie or win
            print("You are early")
            if choice == "rock":
                computer_move = comp_mod_rock[random.randint(0,1)]
                human, computer = win_game(choice,computer_move)
                human_wins += human
                computer_wins += computer
            elif choice == "paper":
                computer_move = comp_mod_paper[random.randint(0,1)]
                human, computer = win_game(choice,computer_move)
                human_wins += human
                computer_wins += computer
            else:
                computer_move = comp_mod_scissors[random.randint(0,1)]
                human, computer = win_game(choice,computer_move)
                human_wins += human
                computer_wins += computer
        elif diff > 0.25 and diff < 0.75:
            #random chance for both players
            computer_move = computer_moves[random.randint(0,2)]
            print("Fair game!")
            human, computer = win_game(choice,computer_move)
            human_wins += human
            computer_wins += computer
        else:
            #player has advantage to tie or win
            print("Cheater! You looked!")
            if choice == "rock":
                computer_move = comp_mod_scissors[random.randint(0,1)]
                human, computer = win_game(choice,computer_move)
                human_wins += human
                computer_wins += computer
            elif choice == "paper":
                computer_move = comp_mod_rock[random.randint(0,1)]
                human, computer = win_game(choice,computer_move)
                human_wins += human
                computer_wins += computer
            else:
                computer_move = comp_mod_paper[random.randint(0,1)]
                human, computer = win_game(choice,computer_move)
                human_wins += human
                computer_wins += computer

        print(f"Human wins: {human_wins} || Computer wins: {computer_wins}")
        choice = playerSelection()

def win_game(choice,computer_move):
    win_conditions= {"rock": "scissors","paper": "rock","scissors": "paper"}
    if choice == computer_move:
        print(f"Draw! Both players threw {choice.capitalize()}")
        human = 1
        computer = 1
        return human, computer
    elif win_conditions[choice] == computer_move:
        print(f"Player wins! {choice.capitalize()} beats {computer_move.capitalize()}!")
        human = 1
        computer =0
        return human, computer
    else:
        print(f"Computer wins! {computer_move.capitalize()} beats {choice.capitalize()}!")
        human = 0
        computer = 1
        return human, computer

def play_RPS():
    choice = playerSelection()
    rpsCountdown(choice)

play_RPS()