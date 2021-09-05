# list, set, dict
my_list = []

for char in 'hello':
    my_list.append(char)

print(my_list)

# list comprehension
new_list = [param for param in 'hello']
new_list2 = [num for num in range(4)]
new_list3 = [num**2 for num in range(5)]
new_list4 = [num**2 for num in range(5) if num%2 ==0]
print(new_list)
print(new_list2)
print(new_list3)
print(new_list4)