# Прототип — это порождающий паттерн, который позволяет
# копировать объекты любой сложности без привязки к их
# конкретным классам.

# Пример паттерна прототип, В котором показывается
# использование какого-то объекта в качестве прототипа,
# а затем его копирование

import copy


class Address:  # Инициализируем класс с адрессом, городом и страной, сохраняем как атрибуты
    def __init__(self, street_address, city, country):
        self.city = city
        self.street_address = street_address
        self.country = country

    def __str__(self):  # метод для вывода данных объекта
        return f"{self.street_address},{self.city},{self.country}"


class Person:
    def __init__(
        self, name, address
    ):  # Инициализируем класс с именем и адрессом, сохраняем как атрибуты
        self.name = name
        self.address = address

    def __str__(self):  # метод для вывода данных объекта
        return f"{self.name} lives at {self.address}"


Dima = Person("Dima", Address("Mira street 25", " Omsk", " Russia"))
 Masha = copy.deepcopy(Dima) #Выпоняет рекурсивную копию всех атрибутов объекта, тем самым создавая совершенно новый объект, Который не ссылается на оригинал
 Masha.name='Masha'
 Masha.address.street_address='Mira street 125'
 print(Dima, '\n', Masha)


# Оба персона ссылаются на один и тот же объект
#print(Dima)
#Masha = Dima
#Masha.name = "Masha"
#print("-----")
#print(Dima)
#print(Masha)
