'''
rock, paper, scissors, lizard, spock
'''

from random import randint


class Player:
    '''
    A class for the player
    '''
    def __init__(self):
        self.choise = ''

    def setChoise(self, choise):
        '''
        Set the choise
        '''
        if choise:
            self.choise = choise

    def getChoise(self):
        '''
        get the choise
        '''
        return self.choise


alternatives = ['r', 'p', 's', 'l', 'sp']
# r = Rock, p = Paper, s = Scissors, l = Lizard, sp = Spock

player = False


def the_game(player):
    '''
    A function to check if the input is valid, if the computer
    wins or the player wins. If the input isn't valid,
    the terminal will ask for the players choise again.
    '''
    player_one = Player()
    player_two = Player()

    while player is False:
        computer = alternatives[randint(0, 4)]
        player_two.setChoise(computer)
        print('Input should be:')
        print('r = rock, s = scissors, p = paper, l = lizard, sp = spock\n')
        player = input('Write your choise here:\n')
        player_one.setChoise(player)

        if player_one.getChoise() == player_two.getChoise():
            print("That's a tie!")
        elif player_one.getChoise() == 'r':
            if player_two.getChoise() == 'p' or player_two.getChoise() == 'sp':
                print("Oh, you lost...")
                print(f'computers choise was: {player_two.getChoise()}')
            else:
                print("You win!")
                print(f'computers choise was: {player_two.getChoise()}')
        elif player_one.getChoise() == 'p':
            if player_two.getChoise() == 's' or player_two.getChoise() == 'l':
                print("Oh, you lost...")
                print(f'computers choise was: {player_two.getChoise()}')
            else:
                print("You win!")
                print(f'computers choise was: {player_two.getChoise()}')
        elif player_one.getChoise() == 's':
            if player_two.getChoise() == 'r' or player_two.getChoise() == 'sp':
                print("Oh, you lost...")
                print(f'computers choise was: {player_two.getChoise()}')
            else:
                print("You win!")
                print(f'computers chose was: {player_two.getChoise()}')
        elif player_one.getChoise() == 'l':
            if player_two.getChoise() == 's' or player_two.getChoise() == 'r':
                print("Oh, you lost...")
                print(f'computers choise was: {player_two.getChoise()}')
            else:
                print("You win!")
                print(f'computers choise was: {player_two.getChoise()}')
        elif player_one.getChoise() == 'sp':
            if player_two.getChoise() == 'p' or player_two.getChoise() == 'l':
                print("Oh, you lost...")
                print(f'computers choise was: {player_two.getChoise()}')
            else:
                print("You win!")
                print(f'computers choise was: {player_two.getChoise()}')
        else:
            print("The input is not valid.")
            print("Are you sure you wrote r, p, s, l or sp?")
            player = False


play_again = ''


def start_over(play_again):
    '''
    Asks the player if he/she wants to play again.
    If y, the game starts again and if n, the loop
    breaks.
    '''
    while True:
        play_again = input('Play again? y/n?\n')

        if play_again == 'y':
            print("You pressed y, let's play again!\n")
            the_game(player)
        elif play_again == 'n':
            print('You pressed n, thanks for playing!')
            break
        else:
            print('Invalid, press y or n')


print('Hi and welcome to "Rock, Paper, Scissors, Lizard, Spock"!\n')
print('The rules are:')
print('Rock beats Scissors and Lizard,')
print('Scissors beats Paper and Lizard,')
print('Paper beats Rock and Spock,')
print('Lizard beats paper and Spock,')
print('Spock beats Rock and Scissors\n')
the_game(player)
start_over(play_again)
