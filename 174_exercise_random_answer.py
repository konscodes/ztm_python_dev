from sys import argv
from random import randint

try:
    if len(argv) != 3:
        print('Not enough arguments provided?')
        start = 1
        end = 5
    else:
        start = int(argv[1])
        end = int(argv[2])
except ValueError:
    print('All arguments have to be integers')
    quit()

def main(start, end):
    game_is_on = True
    print(f'Generating number from range {start, end}')
    answer = randint(start, end)
    print(f'Correct answer: {answer}')
    while game_is_on:
        user_choice = int(input(f'Choose a number from {start} to {end} \n'))
        if user_choice == answer:
            print('Congrats, you won!')
            game_is_on = False
        else:
            print('Try again')
            game_is_on = True

main(start, end)
