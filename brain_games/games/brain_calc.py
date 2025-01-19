# this module contains specific algorithm of a brain_calc game
# where user have to calculate two numbers and operation  (*, +, -)

from random import randint

# constant stores the name of the game
NAME = 'brain_calc'


# print rules to console
def print_rules():
    print('What is the result of the expression?') 
    
    
# print to console two whole numbers (num) and operation (*, +, -) 
# num: min_num <= num <= max_num.
# returns the result of equalation
def print_question_and_return_answer(min_num, max_num):
    operand1 = randint(min_num, max_num)
    operand2 = randint(min_num, max_num)
    operations = {0: '+', 1: '-', 2: '*'}
    # get random number [0..2] to take operation from operations dictionary
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


