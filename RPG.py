import random

'''
    Multiline comments
'''

# single line comments


class Enemy:
    hp = 300

    # initializes
    def __init__(self, atkl, atkh):
        self.atkl = atkl
        self.atkh = atkh

        # This is just to build a function
    def getAtk(self):
        print(self.atkl)

    def getHP(self):
        print("Hp is", self.hp)


# instanced variable
enemy1 = Enemy(40, 49)
enemy1.getAtk()
enemy1.getHP()
enemy2 = Enemy(70, 100)
enemy2.getAtk()
enemy1.getHP()

playerhp = 260
enemyatkl = 30
enemyatkh = 60
specialCounter = 0

print("Welcome to 'Slay The Dragon'")
while playerhp > 0:
    kick = random.randrange(enemyatkl, enemyatkh)
    punch = random.randrange(enemyatkl, enemyatkh)
    special = enemyatkh
    choice = ""
    print("Choose your attack")
    print("Kick, Punch, Special")
    choice = input()
    cleanedChoice = choice.casefold()

    if cleanedChoice == 'kick':
        playerhp = playerhp - kick
        print("He now has", playerhp, "hp")
    if cleanedChoice == 'punch':
        playerhp = playerhp - punch
        print("He now has", playerhp, "hp")
    if cleanedChoice == 'special':
        if specialCounter == 0:
            playerhp = playerhp - special
            specialCounter = +1
            print(specialCounter)
            print("he now has", playerhp, "hp")
        else:
            print("you already used your special")
    if playerhp <= 0:

        print("you have slayed the monster")
        break

# while playerhp > 0:
#     while choice in ['kick', 'punch', or 'special']


