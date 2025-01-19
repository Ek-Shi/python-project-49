# this module contains specific algorithm of a brain_progression game
# where user have to guess the number is missing in the progression

from random import randint

# constant stores the name of the game
NAME = 'brain_progression'
# constant stores minimal step for progression generation
MIN_STEP = -5
# constant stores maximal step for progression generation
MAX_STEP = 5
# constant stores the minimal numbers amount in the progression
MIN_LENGTH = 5
# constant stores the maximal numbers amount  in the progression
MAX_LENGTH = 10


# print rules to console
def print_rules():
    print('What number is missing in the progression?') 
    
    
# print to console progression from LENGTH_OF_PROGRESSION numbers
# num: min_num <= num <= max_num.
# returns the number is missing in the progression 
def print_question_and_return_answer(min_num, max_num):
    first = randint(min_num, max_num)
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


