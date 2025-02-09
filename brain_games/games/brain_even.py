# module contains the even game
# where user have to guess parity of a number


from random import randint

from brain_games.config import MAX_NUMBER, MIN_NUMBER

NAME = 'brain_even'


# print rules to console
def print_rules():
    print('Answer "yes" if the number is even, otherwise answer "no".') 


# return True if the number is even, 
# otherwise return False 
def is_even(number):
    if number % 2 == 0:
        return True
    return False

  
# print to console progression from LENGTH_OF_PROGRESSION numbers
# num: MIN_NUMBER <= num <= MAX_NUMBER.
# guess if number is even
def print_question_and_return_answer():
    operand = randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Question: {operand}')
    result = 'yes' if is_even(operand) else 'no'
    return result

