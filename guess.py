#Imported Random
import random

#Used Random for machine to provide a number in a range 1 - 100
number = random.randint(1,100)

#Player provide their Name
name = input("Player's Name? ") 

#ZGame Introduction
input(f"Welcome to Guess game, {name}\nIf on your guess is right You'd get a Congratulatory message and your number of Trials\nIf your subsequent guess is closer to the number than previous wronged one you get 'WARMER' and otherwise you would get 'COLDER'.\nIf your guess is greater than 100 OR less than 1 you would get 'OUT OF BOUND'\nAnd lastly if your first guess is within the range of '10' to the number you would get WARM and if otherwise COLD\nClick enter to continue and GOODLUCK!!!")

#empty Guess list
guesses = []


#While true for my Guess loop iteration
while True:
    guess = int(input("What is your Guess? "))
    guesses.append(guess)

    if guess<1 or guess>100:
        print("OUT OF BOUND")
        continue
    if guess == number:
        print(f"What a Genius you are, {name}\nYou've guessed this in just {len(guesses)} Trials")
        break
   


    if  len(guesses) == 1:
        if abs(number - guess) <= 10:
            #If I need to cheat my code
            # print(abs(number - guess))
            print("WARM")
        else:
            print("COLD")
    
    else:
        # if len(guesses) > 1:
        if  abs(number - guesses[-1]) <= abs(number - guesses[-2]):
            #If I need to cheat my code
            #print(number - guesses[-1])
               print("WARMER")
            
        else:
               print("COLDER")
               





     




