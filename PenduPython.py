from random import *

player_score = 0
computer_score = 0

def Pendu(pendu):
    graphic = [
    """
        +-------+
        |
        |
        |
        |
        |
    ---------------
    ---------------
    """
        ,
    """
        +-------+
        |       |
        |       O
        |
        |
        |
    ---------------
    ---------------
    """
        ,
    """
        +-------+
        |       |
        |       O
        |       |
        |
        |
    ---------------
    ---------------
    """
        ,
    """
    """
        +-------+
        |       |
        |       O
        |      -|
        |
        |
    ---------------
    ---------------
    """
        ,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |
        |
    ---------------
    ---------------
    """
        ,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |      /
        |
    ---------------
    ---------------
    """
        ,
    """
        +-------+
        |       |
        |       O
        |      -|-
        |      / \
        |
    ---------------
    ---------------
    """]
    print(graphic[pendu])
    return

def start():
    print("Jouons au jeu du Pendu.")
    while game():
        pass
    scores()
    
def game():
    dictionnary = ["développement","web","harry-potter","pingouin","linux","pragmatisme"]
    word = choice(dictionnary)
    word_length = len(word)
    clue = word_length * ["_"]
    tries = 6
    letters_tried = ""
    guesses = 0
    letters_right = 0
    letters_wrong = 0
    global computer_score, player_score
    
    while (letters_wrong != tries) and ("".join(clue) != word):
        letter = guess_letter()
        if len(letter) == 1 and letter.isalpha():
            if letters_tried.find(letter) != -1:
                print("Vous avez déjà joué la lettre ", letter)
            else:
                letters_tried = letters_tried + letter
                first_index = word.find(letter)
                if first_index == -1:
                    letters_wrong +=1
                    print("Désolé", letter, "n'est pas la bonne lettre.")
                else:
                    print("Bravo", letter, "est correcte.")
                    for i in range(word_length):
                        if letter == word[i]:
                            clue[i] = letter
        else:
            print("Faites un autre choix.")
            
        Pendu(letters_wrong)
        print("".join(clue))
        print("Essais : ", letters_tried)
        
        if letters_wrong == tries:
            print("Fin du jeu.")
            print("Le mot était", word)
            computer_score += 1
            break
        return play_again()

def guess_letter():
    print
    letter = input("Devinez le mot mystère :")
    letter.strip()
    letter.lower()
    print
    return letter

def play_again():
    answer = input("Voulez-vous rejouer? o/n: ")
    if answer in ("o", "O", "oui", "Oui", "OUI"):
        return answer
    else:
        print("Merci d'avoir joué, à bientôt pour de nouvelles aventures !")
        
def scores():
    global player_score, computer_score
    print("MEILLEURS SCORES")
    print("Joueur : ", player_score)
    print("Ordinateur : ", computer_score)
    
    if __name__ == '__main__':
        start()
