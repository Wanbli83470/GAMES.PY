import random as r
import time


class Hero:
    def __init__(self, santé=100, bouclier=0):
        self.santé = santé
        self.bouclier = bouclier

    def attack(self):
        return r.randint(10, 20)

    def loss(self, malus):
        print(f"Attaque de : {malus} points")
        self.santé -= malus - self.bouclier/100 * malus
        print(f"Vous avez perdu {malus - self.bouclier/100 * malus} points de santé, il vous reste {self.santé}")

    def care(self):
        self.santé += r.randint(10, 20)
        print(f"Votre héros a gagné des points de santé")
        print(f"Votre héros dispose de {self.santé} points")

    def protect(self):
        if self.bouclier < 0:
            self.bouclier = 5
        self.bouclier += 5
        print(f"Votre bouclier encaisse {self.bouclier}% des dégats")


class Enemy:
    def __init__(self, santé=100, bouclier=0):
        self.santé = santé
        self.bouclier = bouclier

    def attack(self):
        return r.randint(10, 20)

    def loss(self, malus):
        print(f"Attaque de : {malus} points")
        self.santé -= malus - self.bouclier/100 * malus
        print(f"Vous adversaire a perdu {malus - self.bouclier/100 * malus} points de santé, il lui reste {self.santé}")

    def care(self):
        self.santé += r.randint(10, 20)
        print(f"Votre adversaire a gagné des points de santé")
        print(f"Votre adversaire dispose de {self.santé} points")

    def protect(self):
        if self.bouclier < 0:
            self.bouclier = 5
        self.bouclier += 5
        print(f"Votre bouclier encaisse {self.bouclier}% des dégats")


nb_Enemy = 1


class Game:
    hero = Hero()
    ennemy = Enemy()
    while ennemy.santé >= 0 or hero.santé >= 0:
        print(f"You : {hero.santé} \nEnnemy : {ennemy.santé}")
        if hero.bouclier:
            print(f"Votre bouclier est actif {hero.bouclier}%")
        if ennemy.bouclier:
            print(f"Bouclier adverse actif {ennemy.bouclier}%")
        """Action Hero"""
        print("\n")
        choice_hero = int(input("Que souhaitez-vous faire ? \n 1 : Attaquer \n 2 : Se soigner \n 3 : Forger le bouclier\n>>> "))
        if choice_hero == 1:
            attack = hero.attack()
            ennemy.loss(attack)
            if ennemy.bouclier > 0:
                ennemy.bouclier -= 1
        elif choice_hero == 2:
            hero.care()
        elif choice_hero == 3:
            hero.protect()
        """Action Ennemy"""
        time.sleep(2)
        print("\n"*2)
        choice_ennemy = r.randint(1, 3)
        if choice_ennemy == 1:
            attack = ennemy.attack()
            hero.loss(malus=attack)
            if hero.bouclier > 0:
                hero.bouclier -= 1
        elif choice_ennemy == 2:
            ennemy.care()

        elif choice_ennemy == 3:
            ennemy.protect()