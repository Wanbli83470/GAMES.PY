import random as r
number_random = r.randint(0, 100)
user_choice = -1
attempt = 0

while user_choice != number_random:
    user_choice = int(input("Deviner un nombre compris entre 0 et 100, vous avez 10 essaies : >>> "))
    attempt += 1
    if user_choice == number_random:
        print(f"Félicitation ! \nVous avez réussi en {attempt} essais")

    elif attempt >= 10:
        print("Echec, vous avez épuisé tous vos essais !")
        break

    else:
        print(f"Il vous reste : {10-attempt} essais")
        if user_choice > number_random:
            print("Le résultat attendu est plus petit")
        else:
            print("Le résultat attentdu est plus grand")
