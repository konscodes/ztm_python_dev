class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age
        self.mydic = {
            'name': 'tod',
            'has_pets': True
        }

    def __str__(self):
        return f'{self.color}'
    
    def __len__(self):
        return 5
    
    def __call__(self):
        return('yes')
    
    def __getitem__(self, i):
        return self.mydic[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])