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
#         self.age = newagestudent
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

# class Alphed:
#     def __init__(self,lang,letters):
#         self.lang = lang
#         self.letters = letters
#     def alphed(self):
#         return f"alphed: {self.letters} lenght: {len(self.letters)}"
#     def english(self,langi,lettersi):
#         self.langi = langi
#         return f"len: {langi}, letters: {lettersi}, len: {len(lettersi)}"
#     def len(self):
#         return f"len: {len()}"

