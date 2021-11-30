# 136 functional programming start
# 138 pure functions
# Same input always returns same output
# Function shouldn't affect outside world

def multiply_by2(li):
    new_list = [] # no side effects unless list is defined outside of the function
    for item in li:
        new_list.append(item*2)
    return new_list

print(multiply_by2([1,2,3])) # always returns same output

# map, filter, zip and reduce
# map(action, [1,2,3])
my_list = [1,2,3]
def multiply_by2(item):
    return item*2

print(list(map(multiply_by2, my_list)))
print(my_list) # Pure function doesn't change the outside world

# filter
# Filters True or False
def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))
print(my_list) # Pure function doesn't change the outside world

# zip
# Iterates over given items and connects them together
your_list = [10,20,30]
print(list(zip(my_list, your_list)))

# reduce
def accumulator(acc, item):
    print(acc, item)
    return acc + item

from functools import reduce
print(reduce(accumulator, my_list, 0))
