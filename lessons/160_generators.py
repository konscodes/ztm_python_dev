'''
Generators
range(100) - generates numbers 1 by 1
list(range(100)) - creates list of numbers and keeps in memory
'''

def generator_function(num):
    for i in range(num):
        yield i

g = generator_function(10)
print(g)
next(g)
next(g)
print(next(g))