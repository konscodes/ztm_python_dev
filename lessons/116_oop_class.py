# OOP

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def run(self):
        print('run')
        return 'done'


player1 = PlayerCharacter('Duck', 33)
player2 = PlayerCharacter('Tom', 21)
player2.attack = 50

print(player1.name)
print(player2.age)
print(player2.run())
print(player2.attack)