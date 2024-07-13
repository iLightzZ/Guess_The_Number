#C04-15

#Guess The Number game

import random

def guessTheNumber():
    print("\nWelcome to the best game on this planet. Hell, the best game to ever exist. Yep, you guessed it (pun intended), It's the Guess The Number Game!\n");
    print("Rules are pretty straightforward: Guess the number...\n\nOK GOOD LUCK BYE!\n");
    print("psssssst. Don't forget. The number you are trying to guess is from 1 to 1000...\n");
    number = random.randrange(1, 1000); #The number the user has to guess
    tries = 1; #The number of tries 
    
    while(True):
        user_guess = int(input("Enter your guess: "));
         
        if(number == user_guess):
            print("Congratulations! You have guessed the number in",tries,"tries.");
            retry = input("\nWould you like to play again(y or n)?: ");
            if("n" == retry):
                break;
            else:
                number = random.randrange(1, 1000);
                tries = 1;
                print("\n---------------------------------------------------------------------\n");
                continue;
        
        else:
            tries += 1;
            if(user_guess > number):
                print("\nToo high. Try again");
                
            if(user_guess < number):
                print("\nToo low. Try again.");


guessTheNumber();
