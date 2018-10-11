import random
import time

pierre = 1
papier = 2
ciseaux = 3

names = { pierre: "Pierre", papier: "Papier", ciseaux: "Ciseaux" }
rules = { pierre: ciseaux, papier: pierre, ciseaux: papier }

player_score = 0
computer_score = 0

def start():
    print("Faisons une partie de Pierre, Papier, Ciseaux!")
    while game():
        pass
    scores()
    
def game():
    player = move()
    computer = random.randint(1, 3)
    result(player, computer)
    return play_again()

def move():
    while True:
        print
        player = input("Pierre = 1\nPaper = 2\nCiseaux = 3\nFaites un mouvement: ")
        try:
            player = int(player)
            if player in (1,2,3):
                return player
        except ValueError:
            pass
        print("HEY HO! Il faut rentrer 1, 2 ou 3 !!!")
        
def result(player, computer):
    print("1...")
    time.sleep(2)
    print("2...")
    time.sleep(2)
    print("2.3/4...")
    time.sleep(2)
    print("ça devient long non?")
    time.sleep(1.5)
    print("Bon ok 3!")
    time.sleep(1)
    print("Computer a fait {0}!".format(names[computer]))
    global player_score, computer_score
    if player == computer:
        print("Egalité")
    else:
        if rules[player] == computer:
            print("VICTOIRE!! Bravo vous avez terrassé l'ennemi")
            player_score += 1
        else:
            print("Computer se rit de vous, vous avez PERDU LOOSER AH AH AH!!!")
            computer_score += 1

def play_again():
    answer = input("Voulez-vous faire une autre partie? y/n: ")
    if answer in ("y", "Y", "yes", "Yes", "o", "O", "oui", "Oui"):
        return answer
    else:
        print("Merci d'avoir joué à mon jeu. A bientôt pour de nouvelles aventures ! ")
        
def scores():
    global player_score, computer_score
    print("Meilleurs scores")
    print("Player: ", player_score)
    print("Computer: ", computer_score)
    
if __name__ == '__main__':
    start()
