# this module contains specific algorithm of a brain_gcd game
# where user have to find the greatest common divisor of given numbers

from math import gcd
from random import randint

from brain_games.config import MAX_NUMBER, MIN_NUMBER

NAME = 'brain_gcd'


# print rules to console
def print_rules():
    print('Find the greatest common divisor of given numbers.') 
    
    
# print to console two whole numbers (num) 
# num: MIN_NUMBER <= num <= MAX_NUMBER.
# returns the greatest common divisor 
def print_question_and_return_answer():
    operand1 = randint(MIN_NUMBER, MAX_NUMBER)
    operand2 = randint(MIN_NUMBER, MAX_NUMBER)
    print(f'Question: {operand1} {operand2} ')
    result = gcd(operand1, operand2)
    return str(result)


