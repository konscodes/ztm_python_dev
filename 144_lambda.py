# lambda expresions
# lambda param: action(param)
from functools import reduce

my_list = [1,2,3]

def multiply(item):
    return item * 2 # same as lambda item: item*2

def only_odd(item):
    return item % 2 !=0

def accumulator(acc, item):
    return acc + item

print(list(filter(only_odd, my_list)))
print(list(filter(lambda item: item % 2 !=0, my_list)))

print(reduce(accumulator, my_list, 10))
print(reduce(lambda acc, item: acc + item, my_list))

print(list(map(multiply, my_list)))
print(list(map(lambda item: item*2, my_list)))