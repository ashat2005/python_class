# class Student:
#     books = []
#     knowledge = 0
#     is_ready_to_work = False
#     languages = {}
#     def read_books(self,prochyl):
#         self.books.append(prochyl)
#         self.__add_points(100)
#         return f"Вы прочитали {self.books} У вас баллов {self.knowledge}"
#     def do_homework(self):
#         self.__add_points(10)
#     def do_project(self):
#         self.__add_points(50)
#     def __add_points(self, points):
#         self.knowledge += points
#         if self.knowledge >= 1000:
#             print("Этот студент готов к работе")
#             self.is_ready_to_work = True
#         else:
#             print("Этот студент не готов к работе")
#     def learn_new_language(self,yzyk,procs):
#         if procs <=1 or procs>100:
#             return f"у вас не достаточно знаний {procs}%"
            
            
#         else:
#             self.languages.setdefault(yzyk,procs)

#             return f"Вы знаете язык {yzyk} на {procs}%"
        
#     def info(self):
#         return f"Инфо о книге {self.books} Сколько у него баллов {self.knowledge} Он работает {self.is_ready_to_work} На каком языке он {self.languages}"     
# student = Student()
# print(student.info())
# print(student.do_homework())

# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.read_books("prog"))
# print(student.learn_new_language("python",10))
# print(student.info())
##################################
# print("geek")
# print(10)
# print(True)
# print(10 + 10)
# print(10 + 10.05)
# print("geek" + "tech")
# hello = "world"
# print(len(hello))
# lst = ["osh", "bishkek", "batken"]
# for cyti in lst:
#     print(cyti, len(cyti))
# print(len(lst))



# class Dog:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#     def info(self):
#         return f"Dog name: {self.name}, age {self.age}"
#     def make_sound(self):
#         return "gawww"
# class Cat:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def info(self):
#         return f"Cat name: {self.name}, age {self.age}"
#     def make_sound(self):
#         return "muuuuyyyyy"
# class Cow:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#     def info(self):
#         return f"Cow name: {self.name}, age: {self.age}"
#     def make_sound(self):
#         return "mooooooo"
# dog = Dog("Dumbo", 6)
# cat = Cat("myvka", 8)
# cow = Cow("cow", 8)
# for animal in (dog, cat, cow):
#     print(animal.info())
#     print(animal.make_sound())
######################################
# class SlotMachine:
#     name = []
#     __user_balance = 100
#     __game_balance = 0
#     def dop_up_name(self,name):
#         return self.name.append(name)
#     def info(self):
#         return f"Name: {self.name} User-Balance: {self.__user_balance} Game-Balance: {self.__game_balance}"
#     def top_up_balance(self,balance,balanse):
#         if self.__user_balance < 0 and self.__user_balance >=100:
#             return f"не достаточно денег остаток на счёте {self.__user_balance}"
#         else:
#             self.__balance_up(balance)
#             self.__balance_up(balanse)
#             return f"Операция произведена успешно остаток на счёте: {self.__user_balance} Игровой счёт: {self.__game_balance}"
    
#     def __balance_up(self,balance):
#         if balance > 100:
#             return "error"
#         else:
#             self.__user_balance -= balance
#             self.__game_balance += balance
            
# sot = SlotMachine()
# print(sot.info())
# print(sot.dop_up_name("askhat"))
# print(sot.info())
# print(sot.top_up_balance(100,100))
# print(sot.info())
#####################################
# import random
# class SlotMachine:
#     def __init__(self, name):
#         self.name = name
#         self.__user_balance = 100
#         self .__game_balance = 0 
#     def info(self):
#         return f"Name: {self.name}, User-Balance: {self.__user_balance}, Game-Balance: {self.__game_balance}"
#     def top_up_balance(self,balance):
#         if balance <=100:
#             self.__balace_up(balance)
#             return f"{self.name} вы пополнили свой баланс {self.__game_balance}"
#         else:
#             return f"вы можете пополнить баланс до 100$"
#     def __balace_up(self,balance):
#         self.__user_balance -= balance
#         self.__game_balance += balance
#     def game(self):
#         randomi = random.randint(1,10)
#         popytky = 0
#         while True:
#             user = int(input("Ведите число от 1 до 10: "))
#             popytky +=1
#             if randomi == user:
#                 self.__game_balance += 50
#                 return f"Вы выиграли ваш баланс: {self.__game_balance}"
                
#             else:
#                 if 5 - popytky == 0:
#                     self.__game_balance -= 10
                    
#                     return f"Вы проиграли ваш баланс {self.__game_balance}"
                    
#     def conslusion_money(self,money):
#         if money > 50:
#             self.__conslusion_money(money)
#             return f"{self.name} вы пополнили свой баланс {self.__user_balance}"
#         else:
#             return "Вывести можно от 50$"
#     def __conslusion_money(self, money):
#         self.__game_balance -= money
#         self.__user_balance += money

#     def main(self):
#         while True:
#             try:
#                 comanda = int(input("1 - информация, 2 - пополнение игрового баланса, 3 - игра, 4 - перевод денег на основной счёт: "))
#                 if comanda == 1:
#                     print(f"{self.info()}") 
#                 elif comanda == 2:
#                     user = int(input("Cколько вы хотить перевести: "))
#                     if user >= 50:
#                         print(f"{self.top_up_balance(user)}")
#                     else:
#                         print("пополнить можно не меньше 50$")
#                         print(f"{comanda}")
#                 elif comanda == 3:
#                     print(f"{self.game()}") 
#                 elif comanda == 4:
#                     user = int(input("Cколько вы хотить перевести: "))
#                     if user >= 50:
#                         print(f"{self.conslusion_money(user)}")
#                     else:
#                         print("обноличить можно не меньше 50$")
#                 else:
#                     print(comanda)
#             except:
#                 print("Шлюха блять")
# slot = SlotMachine("askhat")
# print(slot.main())
###########################################3
# class Student:
#     def stu(self, name = "Ivan", groupNumber = "10A", age = 18):
#         self.name = name
#         self.groupNumber = groupNumber
#         self.age = age
#         return f"name: {self.name}, group: {self.groupNumber}, age: {self.age}"
#     def getName(self,newstudent):
#         self.name = newstudent
#         return f"Name-Student: {self.name}"
#     def getAge(self,newagestudent):
#         self.age = newagestudentclass Wath:
#     def __init__(self,x,y) -> None:
#         self.x = x
#         self.y = y
#     def add(self):
#         print("Сложение")
#         return f"{self.x + self.y}"
#     def sub(self):
#         print("вычитание")
#         return f"{self.x - self.y}"
#     def mul(self):
#         print("умножение")
#         return f"{self.x * self.y}"
#     def truediv(self):
#         print("деление")
#         return f"{self.x // self.y}"
# a = Wath(100,9)
# print(a.add())
# print(a.mul())
# print(a.sub())
# print(a.truediv())
#         return f"Age-student: {self.age}"
#     def getGroupNumber(self,newgroupstudent):
#         self.groupNumber = newgroupstudent
#         return f"Group-Student: {self.groupNumber}"
#     def SetNameAge(self,newname,newgroup,newage):
#         self.name = newname
#         self.groupNumber = newgroup
#         self.age = newage
#         return f"New-name: {self.name}, new-group: {self.groupNumber}, new-age: {self.age}"
#     def setGroupNumber(self,newgroup):
#         self.groupNumber = newgroup
#         return f"New-name: {self.name}, new-group: {self.groupNumber}, new-age: {self.age}"
# student = Student()
# print(student.stu())
# print(student.getName("jamaldin"))
# print(student.SetNameAge("askhat","11B",19))
# print(student.setGroupNumber("1-21-9"))
# print(student.SetNameAge("askhat","11B",19))
# print(student.getAge(20))
# print(student.getGroupNumber("11"))
########################################
# lst = ["osh", "bishkek", "batken"]
# for cyti in lst:
#     print(cyti, len(cyti))
#################################
# class Hello:
#     def __init__(self,name,surname) -> None:
#         self.name = name
#         self.surname =surname
#     def info(self):
#         return f"{self.name}, {self.surname}"
#     def __str__(self) -> str:
#         return f"str: {self.name}, {self.surname}"
#     # def __repr__(self) -> str:
#     #     return f"Repr: {self.name}, {self.surname}"
#     def __call__(self,new_name):
#         self.name = new_name
        
# hello = Hello("askhat", "kydyrov")
# print(hello)
# hello("zahro")
# print(hello)
###############################################
# from abc import ABC, abstractmethod
# class Math(ABC):
#     def __init__(self,num1,num2):
#         self.num1 = num1 
#         self.num2 = num2 
#     @abstractmethod
#     def add(self):
#         pass
#     @abstractmethod
#     def sub(self):
#         pass
#     @abstractmethod
#     def mult(self):
#         pass
#     @abstractmethod
#     def div(self):
#         pass
# class Sub(Math):
#     def __init__(self, num1, num2):
#         super().__init__(num1, num2)
#     def add(self):
#         return self.num1 + self.num2
#     def sub(self):
#         return self.num1 - self.num2
#     def div(self):
#         return self.num1 / self.num2
#     def mult(self):
#         return self.num1 * self.num2
# sab = Sub(10,10)
# print(sab.add())
#####################################
# class A:
#     color = "red"
#     def hello(self):
#         return "hello"
#     def test(self):
#         return "class A"
# class B:
#     age = 18
#     def world(self):
#         return "world"
#     def test(self):
#         return "class B"
# class C(A,B):
#     def python(self):
#         return "python"
#     def test(self):
#         return "class C"
# c = C()
# print(c.color)
# print(c.hello())
# print(c.age)
# print(c.world())
# print(c.python())
# print(c.test())
###############################
# class CarEngineMixin:
#     def engine(self):
#         return "Мотор"
# class CarDoorMixin:
#     def door(self):
#         return "дверь"
# class CarWeelMixin:
#     def weel(self):
#         return "колесо"
# class carAirBagMixin:
#     def airbag(self):
#         return "подушка безопасности"
# class CarSafetyBeltMixin:
#     def safetybelt(self):
#         return "Ремень безопасности"
# class Car(CarEngineMixin, CarDoorMixin, CarWeelMixin,carAirBagMixin,CarSafetyBeltMixin):
#     def __init__(self,brand,modal,year) -> None:
#         self.brand = brand
#         self.modal = modal
#         self.year = year
# bmw = Car("BMW", "xr5", 2005)
# print(bmw.door())
# print(bmw.weel())
# print(bmw.airbag())
# print(bmw.safetybelt())
#####################################
import random

class GTA:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.money = 100
        self.satiety = 100
        self.walk = 0
        if self.name not in ["Michael", "Trevor", "Franklin"]:
            print("There is no such character")

    def __str__(self):
        return f"Name: {self.name}, Health: {self.health}, Money: {self.money}, Satiety: {self.satiety}, Walk: {self.walk}"

    def do_walk(self):
        self.walk += 1
        return self.walk

    def attack(self, damage):
        if 1 <= damage <= 20:
            print(f"Your character attacked and did damage to {damage}")
        else:
            print("You did no damage")

    def take_damage(self):
        damage = random.randint(1, 50)
        self.health -= damage
        if self.health <= 0:
            self.money -= 10
            self.health = 100
            print(f"Your character took damage {damage} and now has {self.health} health and ${self.money} money")

    def make_money(self):
        self.money += 100
        return self.money

gta = GTA("Michael")
print(gta)
gta.do_walk()
gta.attack(15)
gta.take_damage()
gta.make_money()
print(gta)
