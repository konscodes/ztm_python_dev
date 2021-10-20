# lambda excersise
# Square (to the power of 2)
my_list = [5,4,3]

print(list(map(lambda item: item **2, my_list)))

# List sorting (from lowest based on the second number)
a = [(0,2), (4,3), (9,9), (10, -1)]

b = []
c = []
for t0, t1 in a:
    b.append(t1)
    
b.sort()
print(b)

for item in b:
    for t0, t1 in a:
        if t1 == item:
            new_index = (a.index((t0, t1)))
            c.append(a[new_index])

print(c)

# Lambda sort
a.sort(key=lambda x: x[1])
print(a)