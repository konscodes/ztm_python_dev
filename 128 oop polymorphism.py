class User():
    def sign_in(self):
        print('logged in')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
    
    def attack(self):
        print(f'attacking with {self.arrows} arrows')

wizard1 = Wizard('Tom', 'water')
archer1 = Archer('Bon', 4)

def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

for char in [archer1, wizard1]:
    char.attack()