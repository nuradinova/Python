from openpyxl.utils import datetime


class Car:
    def __init__(self, model: str, vypusk: int, proizvoditel: str,
              volume: float, cvet: str, price: float):
        self.model = model
        self.vypusk = vypusk
        self.proizvoditel = proizvoditel
        self.volume = volume
        self.cvet = cvet
        self.price = price

    def vyvod(self):
        print(f"Model: {self.model}\nvypusk: {self.vypusk}\n"
              f"proizvoditel: {self.proizvoditel}\nvolume: {self.volume}\n"
              f"cvet: {self.cvet}\nprice: {self.price}")


mashine = Car("asj", 2020, "GERMANY", 3.0, "black", 25.000000)
print(mashine.vyvod())

#ZADANIE 2

class Kniga():
    def __init__(self, name: str, god:int, izdatel: str, zhanr: str,
                 author: str, price: int):
        self.name = name
        self.god = god
        self.izdatel = izdatel
        self.zhanr = zhanr
        self.author = author
        self.price = price

    def vyvod(self):
        print(f"Name: {self.name}\nGod: {self.god}\n"
              f"Izdatel: {self.izdatel}\nzhanr: {self.zhanr}\n"
              f"author: {self.author}\nprice: {self.price}")

kniga = Kniga("Jane Eyre", 1885, "Ne pomnyu", "roman", "Bronte", 5000)
print(kniga.vyvod())

#ZADANIE 3

#азвание стадиона, дату открытия, страну, город, вместимость
class Stadion():
    def __init__(self, name: str, data_otkr: datetime, strana: str, vmestimost: int):
        self.name = name
        self.data_otkr = data_otkr
        self.strana = strana
        self.vmestimost = vmestimost


    def vyvod(self):
        print(f"Name: {self.name}\nData otrkytiya: {self.data_otkr}\n"
              f"Strana: {self.strana}\nVmestimost: {self.vmestimost}\n")

kniga = Stadion("Lokomotiv", "26.01.1885", "Kz", 10000)
print(kniga.vyvod())