class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} сел")

    def roll_over(self):
        print(f"{self.name} перекатывается")


my_dog = Dog("Ромка", 3)
my_dog.sit()
my_dog.roll_over()

my_dog = Dog("Димка", 6)
my_dog.sit()
my_dog.roll_over()