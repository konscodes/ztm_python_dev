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

    def check_arrows(self):
        print(f'{self.arrows} arrows remaining')

    def run(self):
        return print('running')

class HybridBorg(Wizard, Archer):
    def __init__(self, name, power, arrows, email):
        Archer.__init__(self, name, arrows, email) # calling Archer init to overcome multiple inheritance
        Wizard.__init__(self, name, power, email)

hybrid1 = HybridBorg('Borgy', 50, 40, 'borg@gmail.com')
print(hybrid1.run())
print(hybrid1.check_arrows()) # multiple inheritance happening here
print(hybrid1.attack())

# MRO - Method resoluton order 

class A:
    num = 10

class B(A):
    pass

class C(A):
    num = 1

class D(B, C):
    pass

print(D.num)
print(D.mro())