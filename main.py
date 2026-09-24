# import json
#
# a = 15
# b = True
# c = {
#     "salom":"muhammadiso",
#     "yil":2013
# }
# a_j = json.dumps(a)
# b_j = json.dumps(b)
# c_j = json.dumps(c)
#
# print(a_j)
# print(b_j)
# print(c_j)
# print(type(a_j))
# print(type(b_j))
# print(type(c_j))
# import json
# a = "true"
# b = "{1:1}"
# print(type(a))
# print(a)
# a2 = json.loads(a)
# print(type(a2))
# print(a2)
# import json
# a = "false"
# b = "{1:1}"
# a2 = json.loads(a)
# print(type(a2))
# print(a2)
# import json
# i = {
#     "isim":"muhammadiso",
#     "faliliya":"mahmudjonov"
# }
# with open("m.iso.json",'w') as f:
#     json.dump(i, f)
#
# dumps paytindan json ga
# loads jsondan paytin ga
# import json
# meva = {
#     "ism": "muhammadiso",
#     "yosh": "1234",
# }
# with open("meva.json", "w") as f:
#     json.dump(meva, f)
#
# with open("meva.json", "r") as f:
#     n = f.read()
#     print(n)
#     print(type(n))
#     meva = json.load(f)
#     print(meva)
#     print(type(meva))
# a = ["olma", "nok", "shaftoli"]
# with open("data.json", "a") as f:
#     print()
# import  json
# info = {
#     "username": "admin",
#     "password": "1234",
#     "email": "242",
# }
# with open("info.json", "w") as f:
#     json.dump(info, f)
# with open("info.json", "r") as f:
#     m = json.load(f)
#     print(m)
#     print(type(m))
# import json
# a = {
#     "isim":"m.iso",
#     "yosh":13
# }
# with open("data.json","w") as f:
#     json.dump(a, f)
# with open("data.json","r") as f:
#     m = json.load(f)
#     print(m)
#     print(type(m))
# import time
# while True:
#      print("sariq chiroq 🟡")
#      time.sleep(1)
#
#      print("yashil chiroq 🟢  qizil 🧍‍🔴 ️")
#      time.sleep(5)
#
#      print("sariq chiroq 🟡")
#      time.sleep(1)
#
#      print("qizil chiroq 🔴   yashil 🚶‍🟢 ️")
#      time.sleep(5)
#
#      print("sariq chiroq 🟡")
#      time.sleep(1)
#
#      print("yashil chiroq 🟢  qizil 🧍‍🔴")
#      time.sleep(5)
#
#      print("sariq chiroq 🟡")
#      time.sleep(1)
#
#      print("qizil chiroq 🔴   yashil 🚶‍🟢")
#      time.sleep(5)
# import time
# while True:
#     print("00:00 dushanba")
#     time.sleep(3)
#     print("07:00 choy ichish")
#     time.sleep(1)
#     print("08:00 maktab ga ketish")
#     time.sleep(4)
#     print("12:10 maktabdan kelish")
#     time.sleep(1)
#     print("12:30 abet qilish")
#     time.sleep(3)
#     print("18:00 kechki ovqat")
#     time.sleep(3)
#     print("21:00 uxlash ")
#     time.sleep(3)
#     print("00:00 seshanba")
#     time.sleep(3)
#     print("07:00 choy ichish")
#     time.sleep(1)
#     print("08:00 maktab ga ketish")
#     time.sleep(3)
#     print("12:10 maktabdan kelish")
#     time.sleep(1)
#     print("12:30 abet qilish")
#     time.sleep(1)
#     print("14:00 dasturlashga borish")
#     time.sleep(3)
#     print("18:00 kechki ovqat")
#     time.sleep(3)
#     print("21:00 uxlash ")
#     time.sleep(3)
#     print("00:00 chorshanba")
#     time.sleep(4)
#     print("07:00 choy ichish")
#     time.sleep(1)
#     print("08:00 maktab ga ketish")
#     time.sleep(3)
#     print("12:10 maktabdan kelish")
#     time.sleep(1)
#     print("12:30 abet qilish")
#     time.sleep(3)
#     print("18:00 kechki ovqat")
#     time.sleep(3)
#     print("21:00 uxlash ")
#     time.sleep(3)
#     print("00:00 chorshanba")
#     time.sleep(4)
#     print("07:00 choy ichish")
#     time.sleep(1)
#     print("08:00 maktab ga ketish")
#     time.sleep(2)
#     print("12:10 maktabdan kelish")
#     time.sleep(1)
#     print("12:30 abet qilish")
#     time.sleep(3)
#     print("18:00 kechki ovqat")
#     time.sleep(3)
#     print("21:00 uxlash ")
#     time.sleep(3)
#     print("00:00 payshanba")
#     time.sleep(3)
#     print("07:00 choy ichish")
#     time.sleep(1)
#     print("08:00 maktab ga ketish")
#     time.sleep(3)
#     print("12:10 maktabdan kelish")
#     time.sleep(1)
#     print("12:30 abet qilish")
#     time.sleep(6)
#     print("14:00 dasturlashga borish")
#     time.sleep(4)
#     print("17:00 kechki ovqat")
#     time.sleep(3)
#     print("21:00 uxlash ")
#     time.sleep(3)
#     print("00:00 juma")
#     time.sleep(3)
#     print("07:00 choy ichish")
#     time.sleep(1)
#     print("08:00 maktab ga ketish")
#     time.sleep(3)
#     print("12:10 maktabdan kelish")
#     time.sleep(1)
#     print("12:30 abet qilish")
#     time.sleep(4)
#     print("18:00 kechki ovqat")
#     time.sleep(3)
#     print("21:00 uxlash ")
#     time.sleep(3)
#     print("00:00 shanba")
#     time.sleep(4)
#     print("07:00 choy ichish")
#     time.sleep(1)
#     print("08:00 maktab ga ketish")
#     time.sleep(3)
#     print("12:10 maktabdan kelish")
#     time.sleep(1)
#     print("12:30 abet qilish")
#     time.sleep(6)
#     print("14:00 dasturlashga borish")
#     time.sleep(3)
#     print("18:00 kechki ovqat")
#     time.sleep(3)
#     print("21:00 uxlash ")
#     time.sleep(3)
#     print("00:00 yak shanba")
#     time.sleep(3)
#     print("07:00 choy ichish")
#     time.sleep(1)
#     print("12:30 abet qilish")
#     time.sleep(3)
#     print("18:00 kechki ovqat")
#     time.sleep(3)
#     print("21:00 uxlash ")
#     time.sleep(3)
# import time
# while True:
#     print("08:10 1-soat")
#     time.sleep(2)
#     print("08:55 tanaffus")
#     time.sleep(2)
#     print("09:00 2-soat")
#     time.sleep(2)
#     print("09:45 tanaffus")
#     time.sleep(2)
#     print("09:50 3-soat")
#     time.sleep(2)
#     print("10:35 tanaffus")
#     time.sleep(2)
#     print("10:45 4-soat")
#     time.sleep(2)
#     print("11:30 tanaffus")
#     time.sleep(2)
#     print("11:35 5-soat")
#     print("12:10 tanaffus")
#     time.sleep(2)
# import datetime
# sana = datetime.date.today()
# print(sana.year)
# print(sana.month)
# print(sana.day)
# import datetime
# s = datetime.date.today()
# print(s.year)
# print(s.month)
# print(s.day)
# print(f"men {s.year} yilning {s.month} -oyida  {s.day} -kunida tug'ilganman")
import time
#
# import datetime
#
# v = datetime.time(23, 59, 59, 999999)
# print(v)
# import datetime, time
# while True:
#     hozir = datetime.datetime.now().strftime("%X:%M:%S")
#     print(hozir)
#     time.sleep(1)
# import datetime
# h = datetime.datetime.now().strftime("%A, %D %B %Y %H:%M:%S %Z,")
# h2 = datetime.datetime.now().strftime("%a, %d %b %h:%m ")
# a = datetime.datetime.now().strftime("%w")
# a2 = datetime.datetime.now().strftime("%m/%d/%Y %I:%M:%S %p")
# print(h)
# print(h2)
# print(a2)
# print(a)
# import de.atetime, time
# # hozir = datetime.datetimnow()
# kelajak = datetime.datetime(2026, 12, 31) -hozir
# print(kelajak)
# import datetime, time
# hozir = datetime.datetime.now()
# kelajak = datetime.datetime(2013, 3, 1, 4) - hozir
# print(kelajak)
# import datetime
# h = datetime.datetime.now()
# k = datetime.datetime(2027, 5, 25) - h
# print(k)
# import datetime
# import time
# while True:
#     soat =  int(input("soat: "))
#     minut = int(input("daqiqa: "))
#     sekund = int(input("sekund: "))
#
#     muddat = datetime.datetime.now()  + datetime.timedelta(hours=soat, minutes=minut, seconds=sekund)
#
#     while datetime.datetime.now() < muddat:
#         qolgan = muddat - datetime.datetime.now()
#         soat = qolgan.seconds // 3600
#         minut = (qolgan.seconds % 3600) // 60
#         sekund = qolgan.seconds % 60
#         print(f"{soat:02}:{minut:02}:{sekund:02}")
#         time.sleep(1)
#     print("\nbo'mba portladi! ")
#     break
# class User():
#     def __init__(self, name,):
#         self.name = name
#
#         user1 = User("Jasur")
#         user2 = User("Diyorbek")
#         user3 = User("Bobur")
# class Name():
#     def __init__(self, name):
#      self.name = name
#      user1 = User("Muhammadiso")
#      user2 = User("maktab")
#      user3 = User("py thon")
# class Maktab():
#  def __init__(self, nom, direktor, manzil, oquvchilar_soni):
#   self.nom = nom
#   self.direktor = direktor
#   self.manzil = manzil
#   self.oquvchilar_soni = oquvchilar_soni
#
#
# maktab1 = Maktab("1-maktab", "Shuhrat ergashev", "Buvayda tumani", 1000)
# n = f"1-maktab:\n"
# n += f"nom:{maktab1.nom}\n"
# n += f"direktor: {maktab1.direktor}\n"
# n += f"manzil: {maktab1.manzil}\n"
# n += f"o'quvchilar soni: {maktab1.oquvchilar_soni}\n"
# print(n)
# class User:
#     def __init__(self, first_name, last_name, email, age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.email = email
#         self.__age = age
#     def __str__(self):
#      return f"{self.first_name} {self.last_name}"
#     def add_age(self):
#         self.__age += 1
#     def update_age(self, age):
#      if age <= 0:
#       print("yoshingizdan ayirib bo'lmaydi!")
#      else:
#         self.__age = age
#     def get_age(self):
#      return self.__age
#     def get_frist_name(self):
#         return self.first_name
# user1 = User("Muhammadiso", "Mahmudjonov", "123miso", 13)
# user2 = User("Bobur", "Qosimov", "123@gmail.com", 21)
# user2.update_age(-276)
# print(user1.get_age())
# print(user2.get_age())
# class User:
#     userlar_soni = 0
#     userlar = []
#     @classmethod
#     def get_userlar(cls):
#         n = f"userlar royhati: {cls.userlar}\n"
#         n += f"userlar soni: {cls.userlar_soni}\n"
#         return n
#     def __init__(self, frist_name, last_name, email, age):
#         self.frist_name = frist_name
#         self.last_name = last_name
#         self.email = email
#         self.__age = age
#         if frist_name == frist_name:
#             print("isimlar bir xil iltimos boshqa ism yozing")
#         User.userlar_soni += 1
#         User.userlar.append(self.frist_name)
# user1 = User("Jasur", "aliyev", "jasur@gmail.com", 28)
# user2 = User("Jasur", "aliyev", "jasur@gmail.com", 28)
# print(User.get_userlar())
# class Ustoz():
#     def __init__(self, ism, yosh):
#         self.ism = ism
#         self.yosh = yosh
#     def get_yosh(self):
#         return self.yosh
#     def get_ism(self):
#         return self.ism
# class Talaba(Ustoz):
#     def __init__(self, ism, yosh, cursi, ovqati):
#         super().__init__(ism, yosh)
#         self.cursi = cursi
#         self.ovqati = ovqati
#     def get_info(self):
#         return f"{self.ism} yoshi {self.yosh} yosh, cursi {self.cursi} ovqati {self.ovqati} "
# ustoz1 = Ustoz("Muhammadiso", 14)
# ustoz2 = Ustoz("ibrohim", 13)
# talaba1 = Talaba("muhammadiso", 14, "python backent", "osh")
# talaba2 = Talaba("ibrohim", 16, "python backent", "omastava")
# print(ustoz1.get_ism())
# print(talaba1.get_info())
# print(ustoz2.get_ism())
# print(talaba2.get_info())














