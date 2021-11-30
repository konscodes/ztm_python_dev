# Decorators
def my_decorator(func):
    def wrap_func():
        print('********')
        func()
        print('********')
    return wrap_func

@my_decorator
def hello():
    print('hellooooo')

hello()

# same as 
# a = my_decorator(hello)
# a()

def my_decorator2(func):
    def wrap_func(*args, **kwargs):
        print('$$$$$$$$')
        func(*args, **kwargs)
        print('$$$$$$$$')
    return wrap_func

@my_decorator2
def hello2(string='hiii', emoji=';)'):
    print(string, emoji)

hello2()