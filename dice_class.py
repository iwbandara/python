import random

class Dice:

    def roll(self):
        # list = ()

        value1 = random.randint(1,6)
        value2 = random.randint(1,6)

        list = value1, value2

        return list

option1 = Dice()

print(option1.roll())
