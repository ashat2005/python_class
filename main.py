# import string


# class Alphed:
#     def __init__(self,lang,letters):
#         self.lang = lang
#         self.letters = letters
#     def print(self):
#         return f"Alphed: {self.letters}"
#     def letters_num(self):
#         return f"lenght: {len(self.letters)}"
# # alphed = Alphed("ru", "йцукенгшщзхъфывапролджэячсмитьбю")

# class English(Alphed):
#     def __init__(self, lang, letters):
#         super().__init__(lang, letters)
#         self.alpehd = string.ascii_uppercase()
#         self.__letters_num = len(self.alpehd)
#     def is_en_letter(self, b):
#         if self.alpehd == b:
#             return f"{self.lang}: {b}"
#         else:
#             return f"no enlish: {b}"
#     def letters_num(self):
#         return f"lenght: {self.__letters_num}"
#     def example(self):
#         return f"nurbolot gay"
# enalphed = English("en","")
# alp= Alphed("ru", "йцукенгшщзфывапролдячсмитьбюжэхъ")
# print(enalphed.letters_num())
# print(enalphed.is_en_letter("askhatbro"))
#############################################################
