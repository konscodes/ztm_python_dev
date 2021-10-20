class User():
    def __init__(self, email):
        self.email = email
    
    def sign_in(self):
        print('logged in')

    def attack(self):
        print('doing nothing')

class Wizard(User):
    def __init__(self, name, power, email):
        User.__init__(self, email) 
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, arrows, email):
        super().__init__(email) # points to the call above without passing self
        self.name = name
        self.arrows = arrows
    
    def attack(self):
        User.attack(self)
        print(f'attacking with {self.arrows} arrows')

wizard1 = Wizard('Tom', 'water', 'tom@gmail.com')
archer1 = Archer('Bon', 4, 'bon@gmail.com')

def player_attack(char):
    char.attack()

player_attack(wizard1)
print(wizard1.email)
print(archer1.email)
