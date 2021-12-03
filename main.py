list1 = ['10110', '10111', '10101']
list2 = ['10110', '10111', '10101', '10000']

data = list(set(list1).difference(list2))
print(data)

print(list(set(list1) & set(list2)))