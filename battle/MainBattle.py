from battle.classes.game import Person, Bcolors
from battle.classes.magic import Spell

# Create Black Magic
fire = Spell("Fire", 10, 100, "Black")
thunder = Spell("Thunder", 10, 100, "Black")
blizzard = Spell("Blizzard", 10, 100, "Black")
meteor = Spell("Meteor", 20, 200, "Black")
quake = Spell("Quake", 14, 140, "Black")

# Create White Magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 10, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]

player = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

running = True
i = 0

print(Bcolors.FAIL + Bcolors.BOLD + "AN ENEMY ATTACKS!" + Bcolors.ENDC)
# END.C makes the traits given to text end

while running:
    print("=================================")
    player.choose_actions()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = player.generate_damage()
        enemy.take_damage(dmg)
        print("You attacked for", dmg, "points of damage.")
    elif index == 1:
        player.choose_magic()
        magic_choice = int(input("Choose magic:")) - 1

        spell = player.magic[magic_choice]
        magic_dmg = spell.generate_spell_dmg()

        current_mp = player.get_mp()

        if spell.cost > current_mp:
            print(Bcolors.FAIL + "\nNot Enough MP\n" + Bcolors.ENDC)
            continue

        player.reduce_mp(spell.cost)
        enemy.take_damage(magic_dmg)
        print(Bcolors.OKBLUE + "\n" + spell.name + " deals", str(magic_dmg), "points of damage" + Bcolors.ENDC)

    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    player.take_damage(enemy_dmg)
    print("Enemy attacks for", enemy_dmg)

    print("============================")
    print("Enemy HP:", Bcolors.FAIL, str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + Bcolors.ENDC + "\n")

    print("Your HP:", Bcolors.OKGREEN, str(player.get_hp()) + "/" + str(player.get_max_hp()) + Bcolors.ENDC + "\n")
    print("Your MP:", Bcolors.OKBLUE, str(player.get_mp()) + "/" + str(player.get_max_mp()) + "\n")

    if enemy.get_hp() == 0:
        print(Bcolors.OKGREEN + "You Win!" + Bcolors.ENDC)
        running = False
    elif player.get_hp() == 0:
        print(Bcolors.FAIL + "Your enemy has defeated you!" + Bcolors.ENDC)
        running = False
