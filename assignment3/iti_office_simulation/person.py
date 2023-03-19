class Person:
    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthRate = healthRate

    def sleep(self):
        self.healthRate += 10

    def eat(self):
        self.healthRate += 5

    def buy(self, amount):
        self.money -= amount
