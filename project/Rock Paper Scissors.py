#Rock Paper Scissor game.
import random
import os
import re
os.system('cls' if os.name=='nt' else 'clear')
while(1 < 2):
    print('\n')
    print('Rock,Paper,Scissors - shoot!')
    userChoice= input('Choose your weapon [R]ock,[P]aper,or [S]cissors:')
    if not re.match('[SsRrPp]',userChoice):
        print('Please choose a latter:')
        print('[R]ock,[S]cissor or [P]aper.')
        continue
    # Echo the user's choice
    print('You chose:'+ userChoice)
    # the opponenet's choice
    choices=['R','P','S']
    opponenetChoice= random.choice(choices)
    print('I chose:'+opponenetChoice)
    #if opponenet and user choice is same.
    if opponenetChoice == str.upper(userChoice):
        print('Tie!')
    #if opponenet Choice Rock  and user choice Paper
    elif opponenetChoice== 'R' and userChoice.upper() =='S': 
        print('Scissors beats rock,I win!')
        continue
    # if opponenet choice Scissior and user choice paper
    elif opponenetChoice== 'S' and userChoice.upper()=='P':
        print('Scissors beats paper! I win!')
        continue
    #if opponenet choice Paper and user choice Rock
    elif opponenetChoice =='P' and userChoice.upper()=='R':
        print('Paper beast rock,i win!')
        continue
    else:
        print('You win!')
