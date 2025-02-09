# this module contains specific algorithm of a brain_progression game
# where user have to guess the number is missing in the progression

from random import randint

from brain_games.config import MAX_NUMBER, MIN_NUMBER

NAME = 'brain_progression'
MIN_STEP = -5
MAX_STEP = 5
MIN_LENGTH = 5
MAX_LENGTH = 10


# print rules to console
def print_rules():
    print('What number is missing in the progression?') 
    
    
# print to console progression from LENGTH_OF_PROGRESSION numbers
# num: MIN_NUMBER <= num <= MAX_NUMBER.
# returns the number is missing in the progression 
def print_question_and_return_answer():
    first = randint(MIN_NUMBER, MAX_NUMBER)
    step = randint(MIN_STEP, MAX_STEP)
    # step can't be 0
    step = MIN_STEP if step == 0 else step
    length = randint(MIN_LENGTH, MAX_LENGTH)
    random_index = randint(0, length - 1)
    result = first + random_index * step
    progression = [str(i) if i != result else '..' 
                    for i in range(first, first + step * length, step)]
    print(f'Question: {' '.join(progression)} ')

    return str(result)


