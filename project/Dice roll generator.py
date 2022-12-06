#Dice roll generator
# import library random for genrating random numbers.
import random
# define minimmum and maximum value of dice.
min_val=1
max_val=6
#for rolling again enter yess or y.
roll_again='yes'
# using while loop for endless roll of dice.
while roll_again=='yes' or roll_again=='y':
    print('Dice rolling....')
    print('The value are:')
    print(random.randint(min_val,max_val))
    print(random.randint(min_val,max_val))
    roll_again=input('Roll the dice again?')
