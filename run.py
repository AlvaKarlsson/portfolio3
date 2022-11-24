# rock, paper, scissors, lizard, spock

from random import randint

alternatives = ['r', 'p', 's', 'l', 'sp']
# r = Rock, p = Paper, s = Scissors, l = Lizard, sp = Spock

computer = alternatives[randint(0, 4)]

print('Hi and welcome to "Rock, Paper, Scissors, Lizard, Spock"!\n')
print('The rules are:')
print('Rock beats Scissors and Lizard,')
print('Scissors beats Paper and Lizard,')
print('Paper beats Rock and Spock,')
print('Lizard beats paper and Spock,')
print('Spock beats Rock and Scissors\n')
print('Input should be:')
print('r = rock, s = scissors, p = paper, l = lizard, sp = spock')

player = False


def the_game(player):
    '''
    A function to check if the input is valid, if the computer
    wins or the player wins. If the input isn't valid,
    the terminal will ask for the players choise again.
    '''
    while player is False:
        player = input('Write your choise here:\n')
        if player == computer:
            print("That's a tie!")
        elif player == 'r':
            if computer == 'p' or computer == 'sp':
                print("Oh, you lost...")
                print(f'computers chose was: {computer}')
            else:
                print("You win!")
                print(f'computers chose was: {computer}')
        elif player == 'p':
            if computer == 's' or computer == 'l':
                print("Oh, you lost...")
                print(f'computers chose was: {computer}')
            else:
                print("You win!")
                print(f'computers chose was: {computer}')
        elif player == 's':
            if computer == 'r' or computer == 'sp':
                print("Oh, you lost...")
                print(f'computers chose was: {computer}')
        elif player == 'l':
            if computer == 's' or computer == 'r':
                print("Oh, you lost...")
                print(f'computers chose was: {computer}')
        elif player == 'sp':
            if computer == 'p' or computer == 'l':
                print("Oh, you lost...")
                print(f'computers chose was: {computer}')
            else:
                print("You win!")
                print(f'computers chose was: {computer}')
        else:
            print("The input is not valid.")
            print("Are you sure you wrote r, p, s, l or sp?")
            player = False


the_game(player)
