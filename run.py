from random import randint

alternatives = ['r', 'p', 's']
#r = Rock, p = Paper, s = Scissors

computer = alternatives[randint(0, 2)]

print('Hi and welcome to "Rock, Paper, Scissors"!\n')
print('The rules are:')
print('Rock beats Scissors, Scissors beats Paper and Paper beats Rock\n')
print('Input should be: r = rock, s = scissors, p = paper')

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
            if computer == 'p':
                print("Oh, you lost...")
                print(f'computers chose was: {computer}')
            else:
                print("You win!")
                print(f'computers chose was: {computer}')
        elif player == 'p':
            if computer == 's':
                print("Oh, you lost...")
                print(f'computers chose was: {computer}')
            else:
                print("You win!")
                print(f'computers chose was: {computer}')
        elif player == 's':
            if computer == 'r':
                print("Oh, you lost...")
                print(f'computers chose was: {computer}')
            else:
                print("You win!")
                print(f'computers chose was: {computer}')
        else:
            print("The input is not valid. Are you sure you wrote r, p or s?")
            player = False

the_game(player)