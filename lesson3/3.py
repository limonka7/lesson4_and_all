class Human:
    default_name = "John"
    default_age = 30

    def __init__(self, name=None, age=None):
        self.name = name if name is not None else Human.default_name
        self.age = age if age is not None else Human.default_age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f"Name: {self.name}, Age: {self.age}, Money: {self.__money}, House: {self.__house}")

    @staticmethod
    def default_info():
        print(f"Default Name: {Human.default_name}, Default Age: {Human.default_age}")

    def make_deal(self, house, price):
        if self.__money >= price:
            self.__money -= price
            self.__house = house
            print(f"{self.name} bought a house!")

    def earn_money(self, amount):
        self.__money += amount

    def buy_house(self, house, discount):
        final_price = house.final_price(discount)
        if self.__money >= final_price:
            self.make_deal(house, final_price)
        else:
            print("Not enough money to buy this house!")


class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def final_price(self, discount):
        return self.price - discount


class SmallHouse(House):
    def __init__(self):
        super().__init__(area=40, price=50000)  # Assuming a default price for a small house

# Вызов справочного метода default_info() для класса Human
Human.default_info()

# Создание объекта класса Human
person = Human()

# Вывод справочной информации о созданном объекте
person.info()

# Создание объекта класса SmallHouse
small_house = SmallHouse()

# Попытка купить созданный дом
person.buy_house(small_house, discount=10000)

# Поправка финансового положения объекта и попытка снова купить дом
person.earn_money(60000)
person.buy_house(small_house, discount=10000)

# Просмотр измененного состояния объекта класса Human
person.info()