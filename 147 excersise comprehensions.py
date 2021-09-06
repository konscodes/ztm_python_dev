some_list = ['a', 'b', 'c', 'd', 'b', 'f', 'c']
duplicates = []

# for loop approach
for item in some_list:
    if some_list.count(item) > 1:
        duplicates.append(item)

duplicates_into_set = set(duplicates)
output = ' '.join(duplicates_into_set)
print(f'Duplicated values: {output}')

# lambda approach
lambda_set = set(filter(lambda item: some_list.count(item) > 1, some_list))
output = ' '.join(lambda_set)
print(f'Duplicated values: {output}')

# comprehension approach
duplicates_set = {item for item in some_list if some_list.count(item) > 1}
output = ' '.join(duplicates_set) 
print(f'Duplicated values: {output}')