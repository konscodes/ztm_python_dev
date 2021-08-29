from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capital_letters(word):
    return word[0].upper() + word[1:]

print(list(map(capital_letters, my_pets)))


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]
my_numbers.sort()
print(list(zip(my_strings, my_numbers)))


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]
winning_score = []

def filter_function(item):
    return item > 50

print(list(filter(filter_function, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?
def sum_func(acc, item):
    print(acc, item)
    return acc + item

print(reduce(sum_func, (my_numbers + scores)))