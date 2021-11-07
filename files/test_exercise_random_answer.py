from sys import argv
from random import randint


def continue_input(user_choice, answer):
    if user_choice == answer:
        print('Congrats, you won!')
        return False
    else:
        print('Try again')
        return True


def main(start, end):
    game_is_on = True
    print(f'Generating number from range {start, end}')
    answer = randint(start, end)
    print(f'Correct answer: {answer}')
    while game_is_on:
        try:
            user_choice = int(input(f'Choose a number from {start} to {end} \n'))
            if continue_input(user_choice, answer) == False:
                break
        except ValueError as err:
            print('Input should be an int')
            continue

if __name__ == '__main__':
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
    
    main(start, end)
