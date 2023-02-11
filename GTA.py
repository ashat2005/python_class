# from random import randint



# class GTA:
#     health = 100
#     money = 100
#     satiety = 100
#     walk = 0    
#     damage = randint(0, 20)
#     hurts = randint(0, 100)


#     def __init__(self, character) -> None:
#         self.pers = character
    
       


#     def all(self):
#         return f"Персонаж: {self.pers} \n"\
#                f"Здоровье: {self.health} \n"\
#                f"Деньги: {self.money} \n"\
#                f"Голод: {self.satiety} \n"\
#                f"Ходьба: {self.walk}\n"
    
#     def walks(self):
#         self.walk = self.walk + 1
#         return f"Ходьба: {self.walk}"
        

#     def attack(self):
#         if 1 <= self.damage <= 20:
#             return f"Ваш персонаж атаковал и нанес {self.damage} единиц урона"
#         else:
#             return "Вы не нанесли урон"
        

#     def hurt(self):
#         self.health = self.health - self.hurts
#         if self.health == 0:
#             self.money -= 10
#             self.health += 100
#             return f"Вы умерли! Ваше здоровье восстановлено. Здоровье: {self.health} Списано 10 долларов за лечение. Баланс: {self.money}"
#         else:
#             print( f"Ваш персонаж получил {self.hurts} единиц урона")
#             return f"У вас осталось {self.health} здоровья."

#     def earn_money(self):
#         self.money += 100
#         return f"Вы заработали 100 долларов! Ваш баланс: {self.money}"
# a = GTA("fadfds")
# print(a.all())
# print(a.walks())
# print(a.attack())
# print(a.hurt())
# print(a.earn_money())
class A:
    def __init__(self,a) -> None:
        self.a = a 
    def run(self):
        print(f"run {self.a}")
class B:
    def run(self):
        print("no run")
class D(A,B):
    def Run(self):
        print("run run go away")

human = D("adil")
print(human.run())