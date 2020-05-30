import random

list_word = []
words = str
with open("liste_francais.txt", 'r') as f:
    for l in f:
        if l != "\n":
            list_word.append(l)

list_word = [f.lower() for f in list_word if len(f) < 8]
mot = random.choice(list_word)
mot = list(mot[0:-1])
nb_letter = len(mot)
user_mot = "_" * nb_letter
user_mot = list(user_mot)
tentative = 0
letter_get = []
no_letters = []
while user_mot != mot:
    print(user_mot)
    print(f"{nb_letter} caractères")
    if tentative >= 20:
        print("Echec")
        print(f"Le mot complet était {mot}")
        break
    if len(no_letters) > 0:
        print(f"Lettres testés {no_letters}")
    print("\n")
    letter_user = input("Choissisez une lettre : ")
    if letter_user.lower() in mot:
        print("detection")
        letter_get.append(letter_user.lower())
        user_mot = []
        for l in mot:
            if l in letter_get:
                user_mot.append(l)
            else:
                user_mot.append("_")
    if user_mot == mot:
        print(f"Bravo le mot était bien {mot}")
    else:
        tentative += 1
        no_letters.append(letter_user.lower())
        print(f"Il vous reste {20-tentative} tentatives")