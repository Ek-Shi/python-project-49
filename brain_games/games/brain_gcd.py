# this module contains specific algorithm of a brain_gcd game
# where user have to find the greatest common divisor of given numbers

from math import gcd
from random import randint

# constant stores the name of the game
NAME = 'brain_gcd'


# print rules to console
def print_rules():
    print('Find the greatest common divisor of given numbers.') 
    
    
# print to console two whole numbers (num) 
# num: min_num <= num <= max_num.
# returns the greatest common divisor 
def print_question_and_return_answer(min_num, max_num):
    operand1 = randint(min_num, max_num)
    operand2 = randint(min_num, max_num)
    print(f'Question: {operand1} {operand2} ')
    result = gcd(operand1, operand2)
    return str(result)


