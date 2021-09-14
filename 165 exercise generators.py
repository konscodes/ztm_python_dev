# Fibonacci exercise
# Fn = Fn-2 + Fn-1
# 0 1 1 2 3 5 8

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        prev_a = a
        a = b
        b = prev_a + b

# List version
def fib2(num):
    a = 0
    b = 1
    result = []
    for i in range(num):
        result.append(a)
        prev_a = a
        a = b
        b = prev_a + b
    return result

for x in fib(20):
    print(x)

for x in fib2(20):
    print(x)