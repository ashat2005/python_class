import random

class GTA:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.money = 100
        self.satiety = 100
        self.walk = 0
        # if self.name not in ["Michael", "Trevor", "Franklin"]:
        #     return f"There is no such character"
        
    def proverka(self):
        if self.name == "Michael":
            return f"your character has been selected, your characted: {self.name}"
        elif self.name == "Trevor":
            return f"your character has been selected, your characted: {self.name}"
        elif self.name == "Franklin":
            return f"your character has been selected, your characted: {self.name}"
        else:
            return f"There is no such character"
    def __str__(self):
        
        return f"Name: {self.name}, Health: {self.health}, Money: {self.money}, Satiety: {self.satiety}, Walk: {self.walk}"

    def do_walk(self):
        self.walk += 1
        return self.walk

    def attack(self, damage):
        if 1 <= damage <= 20:
            return f"Your character attacked and did damage to {damage}"
        else:
            return "You did no damage"

    def take_damage(self):
        damage = random.randint(1, 50)
        self.health -= damage
        if self.health <= 0:
            self.money -= 10
            self.health = 100
            return f"Your character took damage {damage} and now has {self.health} health and ${self.money} money"

    def make_money(self):
        self.money += 100
        return self.money

gta = GTA("dgfhjbk")
print(gta.proverka())
print(gta)
gta.do_walk()
gta.attack(15)
gta.take_damage()
gta.make_money()
print(gta)
