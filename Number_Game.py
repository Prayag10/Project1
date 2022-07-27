# Interactive Guess the Number Game 

"""

    The computer will think of a random number from 1 to 10 as 
    secret number.
    Then ask you ( Player ) to guess the number and store as 
    guess number.

    Compare the guess number with the secret number.
    
    If the player guesses the right number he wins, 
    so print player wins and computer lose.
    
    If the player guesses the wrong number, 
    then he loses so print player lose and computer wins.

"""

#The computer will think of a random number from 1 to 10 as 
#    secret number.

import random

secret_number = random.randint(1,10)


    
#Then ask you ( Player ) to guess the number and store as 
#guess number.

guess = int(input("Guess the number between 1 and 10: "))


#Compare the guess number with the secret number.

    
#If the player guesses the right number he wins, 
#so print player wins and computer lose.
    
#If the player guesses the wrong number, 
#then he loses so print player lose and computer wins.

if (guess  == secret_number):
    print ("Player wins and computer loses")
else:
    print ("Player loses and computer wins")
    
    

