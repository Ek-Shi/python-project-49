# this module contains specific algorithm of a brain_prime game
# where user have to guess if number is prime

from random import randint

# constant stores the name of the game
NAME = 'brain_prime'


# print rules to console
def print_rules():
    print('Answer "yes" if given number is prime. Otherwise answer "no".') 


# return true if the number is prime otherwise returns false
def is_prime(number):
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
    return True


# print to console two whole numbers (num) 
# num: min_num <= num <= max_num.
# returns "yes" if given number is prime. Otherwise returns "no"
def print_question_and_return_answer(min_num, max_num):
    operand = randint(min_num, max_num)
    print(f'Question: {operand}')
    result = 'yes' if is_prime(operand) else 'no'
    return result


