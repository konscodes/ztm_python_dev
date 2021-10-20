# Error handling

# sum 1 + 2 in a function
# Exception for error string + num
# Get error description

def summ(num1, num2):
    try:
        print(num1 + num2)
    except TypeError as err:
        print('enter 2 numbers')
        print(f'Message: {err}')

summ(1, '2')