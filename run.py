from random import randint

alternatives = ['r', 'p', 's']
#r = Rock, p = Paper, s = Scissors

computer = alternatives[randint(0, 2)]

def start_game():
    '''
    Welcome message so the player knows the rules, how to input their choise
    and where to write the input
    '''
    print('Hi and welcome to "Rock, Paper, Scissors"!\n')
    print('The rules are:')
    print('Rock beats Scissors, Scissors beats Paper and Paper beats Rock\n')
    print('Input should be: r = rock, s = scissors, p = paper')

    players_choise = input('Write your choise here:\n')

start_game()
