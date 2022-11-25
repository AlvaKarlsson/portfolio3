# Rock, Paper, Scissors, Lizard, Spock
A terminal game for the ones that love the usual rock, paper, scissor game but wants something extra. Instead of the usual game, there is two more alternatives to choose that have different outcomes depending on the computers choise. 

[Here is a link to the deployed site](https://rock-paper-scissors-special.herokuapp.com/)

![Responsive design](https://user-images.githubusercontent.com/114992573/203925275-246d0f4b-f226-4b36-9e73-3d7cd062f85b.png)

## How it works
The game is bery similar to the original game "rock, paper, scissors". The differens is that the alternatives Lizard and Spock has been added. This is from the TV-show "The Big Bang Theory" from the start and has since that grown outside the series fandom.

The rules are simple: Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock, Spock vaporizes rock, and as it always has, rock crushes scissors (As Sheldon himself explains it in the episode). I the deployed verison, the rules are not written in this exact way. It is a bit more "compressed" so the user easily sees what alternative beats the other.

The player will have to chose what you want to play, rock, paper, scissors, lizard or spock. After submitting the answer, the computers choise will apear on the screen and a text that says if there was a tie, the player won or the computer won. Then the player will be asked to play again, and by writing 'y' or 'n' there will be different outcomes. If the player writes 'y', the terminal will ask for another choise and restart the game. If the player writes 'n', then the terminal will write out "You pressed 'n', thanks for playing!" and stop running.

## Features
- The computer is the opponent and its' choise are always randomized

![Computer](https://user-images.githubusercontent.com/114992573/203928181-740c1a5e-a557-4a02-8d15-144d26d235f4.png)

- Easy input to make the game as easy as possible to play

![Choise](https://user-images.githubusercontent.com/114992573/203928334-1081827f-fcfc-4182-9322-35fc5cd97849.png)

- If the input isn't valid, the terminal will tell the user right away

![Invalid](https://user-images.githubusercontent.com/114992573/203929206-b6951dfe-4466-41a1-9c55-bc0cd5ade98a.png)

- After the round is done, the player have the option to play again or stop
  - If the player writes n, the game will stop
  
![Play again n](https://user-images.githubusercontent.com/114992573/203928646-3399b3b0-c089-4ec3-8e45-839f411f9828.png)

  - If the player writes y, the game starts over
  
![Play again y](https://user-images.githubusercontent.com/114992573/203928852-bdf73e8c-9a8e-4653-a9fb-60be464a7f14.png)

## Data Model
To include some type of data model, I chose to do a Player class as a model that worked with the type of project I constructed.

The class stores the choises both the computer and the player has and are later compared with eachother to see who won or not.

## Testing
The code has been tested in different ways to make sure it works in every way.

- All written code passed the PEP8 test with no errors 
- The game works within the deployed Heroku terminal 
- I have also tried to give tha terminal invalid types of input and the error message appropriate for the ocation is shown to the user

## Bugs
- No bugs found or remaining in the code when deployed

## Deployment
- The deployed version of the project works via Code Institute's mock terminal on the Heroku page.
- The original code was written in GitPod

Deployment step by step:
- Create new app in Heroku
- Add buildpacks to the app called Python nad NodeJS
  - Important to have them in that order!
- Choose way of deployment, I chose "Manual Deploy"
- Then press deploy and Heroku deploys the project so it's ready to go

## Credits
- Code Institute for the deployment guide
