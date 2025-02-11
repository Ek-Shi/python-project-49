# module launches all the games
# it contain common algorithm of running the game
# to start the game call run_the_game(game_module) in the main function
# parameter game_module is the module name: 
#  'brain_calc','brain_gcd'...
# each of this modules has two functions:
# print_rules() - print rules to console
# print_question_and_return_answer(min_num, max_num) 
#     generates numbers: min_num <= num <= max_num
#     prints question to console
#     calculates and return answer

from importlib import import_module

from prompt import string

from brain_games.cli import welcome_user

GAMES_COUNT = 3 


# function launches the game
# parameter game_module contains the name the module 
# which describes the game the user wants to play
def run_the_game(game_name):
    game_module = import_game_module(game_name)
    game_name = game_module.NAME
    # print name of the game
    print(f'{game_name}\n')
    # run gritting function
    name = welcome_user()
    game_module.print_rules()
    # run the game GAMES_COUNT times
    for i in range(GAMES_COUNT):
        right_answer = \
            game_module.print_question_and_return_answer()
        user_answer = string('Your answer: ')
        if user_answer == right_answer:
            print_if_right_answer()
        else:
            print_if_wrong_answer(user_answer, right_answer)
            print(f'Let\'s try again, {name}!')
            return
    # if the user got through all the steps, he won
    print(f'Congratulations, {name}!')


# imports game module dynamically by its name
def import_game_module(name):
    return (import_module(f'brain_games.games.{name}'))


# print the message in case user was right    
def print_if_right_answer():
    print('Correct!')


# print the message in case user was wrong    
def print_if_wrong_answer(user_answer, right_answer):
    print(f'"{user_answer}" is wrong answer ;(. '
          f'Correct answer was "{right_answer}".')

