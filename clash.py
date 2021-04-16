# liste pour les insulte

from random import randint 

LIST_1 = ["j'ai besoins ", "tu est tellement moche ", "tu merite meme pas ", "tu est sur ", "je pense ", "pour moi ", "je suis sur "]

LIST_2 = ["de ", "que ", "tu ", "mon ", "ma ", "tu n'a ", "tu ne ", "je "]

LIST_3 = ["ta soeur ", "ton pere ", "ta mere ", "ton chien ", "ta famille ", "ton crâne ", "t'es yeux ","t'es cheveux ", "mes lunette ", "mon casque ", "ton cerveau ", "te regarde ",]

LIST_4 = ["ressemble a un cheval ", "pour te regarder ","son moisie ", "pour déchiffrer ta face ", "son ecarter ", "tellement t moche ", "tellement tu pue ", "est arrondie ", "est diforme ", "est minuscule ", "est gros ",]

LIST_TOTAL = [LIST_1, LIST_2, LIST_3, LIST_4]

def choixlist(type):
    if type == 1 :
        return LIST_1[randint(0, len(LIST_1) - 1)]
    elif type == 2 :
        return [LIST_2[randint(0, len(LIST_2) - 1)] for x in range(2)]
    elif type == 3 :
        return LIST_3[randint(0, len(LIST_3) - 1)]
    else :
        return LIST_4[randint(0, len(LIST_4) - 1)]