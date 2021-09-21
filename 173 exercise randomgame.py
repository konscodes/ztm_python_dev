from sys import argv
from random import choice

try:
    if len(argv) != 3:
        print('Not enough arguments provided?')
        from_this_number = 1
        to_this_number = 5
    else:
        from_this_number = int(argv[1])
        to_this_number = int(argv[2])
except ValueError:
    print('All arguments have to be integers')
    quit()

def random_picker(start=1, end=5):
    global result
    sequence = range(start, end)
    print(f'Generating number from range {sequence}')
    result = choice(sequence)
    print(f'Result: {result}')
    return result

def main():
    game_is_on = True
    while game_is_on:
        user_choice = int(input(f'Choose a number from {from_this_number} to {to_this_number} \n'))
        if user_choice == result:
            print('Congrats, you won!')
            game_is_on = False
        else:
            print('Try again')
            game_is_on = True

result = 0

random_picker(from_this_number, to_this_number)
main()
