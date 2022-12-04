#here we we are designing a simple quiz game .
print(" Welcome To My Quiz Game \n Interesting Game to Play")
Player = input(" Do you want to play the game? \n" )
if Player.lower() != 'yes':
    print("Good Bye")
    quit()  

name_player = input("Enter Your Name: ")

print("Let's Start the Game :) ",name_player)

score = 0

#question:-1
answer = input(' mumbai is also konwn as ? \n ')
if answer.lower() == 'financial capital of india':
    print("Correct")
    score += 1
else:
    print('Wrong')

#question :-2 
answer = input(' Capital of india? \n ')
if answer.lower() == 'delhi':
    print("Correct")
    score += 1
else:
    print('Wrong')

#question :-3
answer = input(' national sport of india? \n ')
if answer.lower() == 'hockey':
    print("Correct")
    score += 1
else:
    print('Wrong')

#question:-4
answer = input(' national bird of india? \n ')
if answer.lower() == 'peacock':
    print("Correct")
    score += 1
else:
    print('Wrong')

#question-5
answer = input(' what type of country india is democratic or monarchy? \n ')
if answer.lower() == 'democratic':
    print("Correct")
    score += 1
else:
    print('Wrong')
    
print("You got the " + str(score)+ " correct answers")
print("You got the " + str((score/5) *100)+ " correct answers")
