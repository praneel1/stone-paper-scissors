import random as r

gameState = True
# KEY:    1=Stone,    2=Paper,    3=Scissors

score = 0
games = 0

while gameState:

    games += 1

    player_choice = input("What do you choose? (Stone = 1) , (Paper = 2) , (Scissors = 3) , (Quit = q ) \n")
    
    if player_choice == "q":
        break

    try:
        player_choice = int(player_choice)
    except ValueError:
        print("Write an actual number. Try again")
        continue

    if player_choice > 4:
        print("Invalid number")
        continue

    
    comp_choice = r.randint(1,3)

    comp_choiceNum = None
    if comp_choice == 1:
        comp_choicename = "Stone"

    elif comp_choice == 2:
        comp_choicename = "Paper"

    else:
        comp_choicename = "Scissors"


    player_choicename = None
    if player_choice == 1:
        player_choicename = "Stone"

    elif player_choice == 2:
        player_choicename = "Paper"

    else:
        player_choicename = "Scissors"


    if player_choice == 3 and comp_choice == 1:
        print("I choose", comp_choicename, ". You choose", player_choicename, ". You Lose \n\n")

    elif player_choice == 1 and comp_choice == 3:
        print("I choose", comp_choicename, ". You choose", player_choicename, ". You Win \n\n")
        score+=1

    elif player_choice > comp_choice:
        print("I choose", comp_choicename, ". You choose", player_choicename, ". You Win \n\n")
        score+=1

    elif player_choice < comp_choice:
        print("I choose", comp_choicename, ". You choose", player_choicename, ". You Lose \n\n")

    elif player_choice == comp_choice:
        print("I choose", comp_choicename, ". You choose", player_choicename, ". Draw. Nobody Wins \n\n")

    else:
        print("Couldn't Process")

winRate = (score/games)*100

print("You beat me", score,"out of", games, "times. Thats a winrate of", winRate, "%. Wow!")