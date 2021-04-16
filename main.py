from personnage import player

from clash import *

def CheckScore(nbr, L) : 
    punchline = ''
    if len(str(nbr)) >= 3 and len(str(nbr)) < 6 :
        for number in str(nbr) :
            punchline += L[int(number) - 1] 
        return punchline
    else : 
        return "une phrase trop petite"

def main() : 
    print("Bienvenue dans NARDINEMOUKE !")
    value = input("Veuillez choisir un personnage, parmi : \n- goku\n- vegeta\n- melito\n- gougoutman \n ==> ")
    player1 = player(value)
    value = input("\nJoueur 2 veuillez choisir votre personnage : ")
    player2 = player(value)
    print("C'EST PARTTIIII !! \n\n")
    
    tour = 0
    while True : 
        L = choixlist(2)
        L.append(choixlist(1))
        L.append(choixlist(3))
        L.append(choixlist(4))
        print("Voici vos attaques : ", L)
        value = int(input("Quel combo voulez vous utiliser ? "))
        attack = CheckScore(value, L)
        if tour % 2 == 0 :
            print(player1.name, "a dit ", attack)
            print("sheeeesh\n\n\n")
            player2.pv -= len(attack) * player1.attack // player2.deffense
            if player2.pv > 0 :
                print("Il vous reste ", player2.pv, " pv")
            else :
                print(player1.name, " a gagné")
                return     
        else :
            print(player2.name, "a dit ", attack)
            print("sheeeesh\n\n\n")
            player1.pv -= len(attack) * player2.attack // player1.deffense
            if player1.pv > 0 :
                print("Il vous reste ", player1.pv, " pv")
            else :
                print(player2.name, " a gagné")
                return  

        L = []
        tour += 1
        
        
main()

        

    


    