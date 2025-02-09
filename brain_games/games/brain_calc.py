# this module contains specific algorithm of a brain_calc game
# where user have to calculate two numbers and operation  (*, +, -)

from random import randint

from brain_games.config import MAX_NUMBER, MIN_NUMBER

NAME = 'brain_calc'


def print_rules():
    print('What is the result of the expression?')   
    
    
# print to console two whole numbers (num) and operation (*, +, -) 
# num: MIN_NUMBER <= num <= MAX_NUMBER.
# returns the result of equalation
def print_question_and_return_answer():
    operand1 = randint(MIN_NUMBER, MAX_NUMBER)
    operand2 = randint(MIN_NUMBER, MAX_NUMBER)
    operations = {0: '+', 1: '-', 2: '*'}
    operation_code = randint(0, 2)
    # pytnon has function eval to calculate expression
    # but I like this old fashioned style
    operation = operations.get(operation_code, '+')
    match operation:
        case '+': 
            result = operand1 + operand2
        case '-': 
            result = operand1 - operand2
        case '*': 
            result = operand1 * operand2
        case '_': 
            operation = '+'
            result = operand1 + operand2
    print(f'Question: {operand1} {operation} {operand2} ')
    return str(result)


