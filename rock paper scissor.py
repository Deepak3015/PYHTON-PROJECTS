import random

def play():
    user = input("s for scisor and p for paper r for rock")
    computer = random.choice( ["r","s","p"])

    if user == computer:
        return "its a tie"
    
    if is_win(user,computer):
        return "you won"
    return "you loose"

    

def is_win(player,opponent):
    if(player =="r"and opponent == "s") or (player == "s" and opponent == "p") or (player == "p" and opponent == "r"):
        return True
    

print(play())
    
