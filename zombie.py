import random

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack_power = random.randint(8, 12)
        self.alive = True
        self.potions = 3
        self.max_potions = 3

    def attack(self):
        return random.randint(8, 12)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Health: {self.health}")
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} has died.")

    def use_potion(self):
        if self.potions > 0:
            heal = 30
            self.health = min(100, self.health + heal)
            self.potions -= 1
            print(f"{self.name} used a potion and healed to {self.health}. Potions left: {self.potions}")
        else:
            print("No potions left!")

    def restore_potion(self):
        if self.potions < self.max_potions:
            self.potions += 1
            print(f"{self.name} found a potion! Total potions: {self.potions}")
        else:
            print(f"{self.name} already has max potions ({self.max_potions}). No extra potion added.")


class Zombie:
    def __init__(self, wave):
        self.name = f"Zombie #{wave}"
        self.health = 60 + wave * 5
        self.attack_power = random.randint(6, 10)
        self.alive = True

    def attack(self):
        return random.randint(6, 10)

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} took {damage} damage. Health: {self.health}")
        if self.health <= 0:
            self.alive = False
            print(f"{self.name} has been destroyed!")



# ---- Game Loop ---- #
player = Player("Hero")
wave = 1

while player.alive:
    print(f"\n--- Wave {wave} ---")
    zombie = Zombie(wave)

    while zombie.alive and player.alive:
        print(f"\n{player.name}'s Health: {player.health} | Potions: {player.potions}")
        print(f"{zombie.name}'s Health: {zombie.health}")

        try:
            choice = int(input("\nChoose Action: 1) Attack  2) Use Potion: "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if choice == 1:
            damage = player.attack()
            zombie.take_damage(damage)
        elif choice == 2:
            player.use_potion()
        else:
            print("Invalid choice.")
            continue

        if zombie.alive:
            damage = zombie.attack()
            player.take_damage(damage)

    if player.alive:
        print(f"\nYou defeated {zombie.name} in Wave {wave}!")
        # Restore potion every 2 waves
        if wave % 2 == 0:
            player.restore_potion()

        cont = input("Continue to next wave? (y/n): ").lower()
        if cont != 'y':
            print("You chose to exit. Good game!")
            break
        wave += 1
    else:
        print(f"\nGame Over! You died in Wave {wave}.")
