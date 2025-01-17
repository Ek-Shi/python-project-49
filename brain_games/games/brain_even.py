# module contains the even game
# where user have to guess parity of a number


from random import randint

from prompt import string

from brain_games.cli import welcome_user

# constant stores the number of times the game will be launch
GAMES_COUNT = 3
# constant stores minimum number to show in the game 
MIN_NUMBER = 10
# constant stores maximum number to show in the game
MAX_NUMBER = 99


# check if answer contains yes expression 
# if it's the string 'yes'
# then return True
# otherwise return False 
def is_yes(answer):
    if answer == 'yes':
        return True
    return False
    

# return opposite answer
# for example if answer = 'yes' function returns 'no'
def opposite_answer(answer):
    if is_yes(answer):
        return 'no'
    return 'yes'


# return True if the number is even, 
# otherwise return False 
def is_even(number):
    if number % 2 == 0:
        return True
    return False
    
    
# print the message in case user was right    
def print_if_right_answer():
    print('Correct!')


# print the message in case user was wrong    
def print_if_wrong_answer(user_answer, right_answer):
    print(f'"{user_answer}" is wrong answer ;(. '
          f'Correct answer was "{right_answer}".')


# function launches the game
def run_brain_even():
    # print name of the game
    print('brain_even\n')
    # run gritting function
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    # run the game GAMES_COUNT times
    for i in range(GAMES_COUNT):
        number = randint(MIN_NUMBER, MAX_NUMBER)
        print(f'Question: {number}')
        answer = string('Your answer: ')
        if is_yes(answer) == is_even(number) and answer in ('yes', 'no'):
            print_if_right_answer()
        else:
            print_if_wrong_answer(answer, opposite_answer(answer))
            print(f'Let\'s try again, {name}!')
            break
        # if the user got through all the steps, he won
        if i == GAMES_COUNT - 1:
            print(f'Congratulations, {name}!')
