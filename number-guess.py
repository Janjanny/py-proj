# import libraries
import random


# take user inputs
lowNum = int(input("Enter low num: "))
highNum = int(input("Enter high num: "))

# setup
randomNum = random.randint(lowNum, highNum)
totalChances = random.randint(lowNum, highNum)

# init number of tries
count = 0
flag = False

print("You have ", totalChances, " to guess the correct number. You may start now")

while count < totalChances:
    count += 1

    # take guess input
    guess = int(input("guess a number: "))

    #condition 
    if guess == randomNum:
        print("Congratulations you did it in ", count, " try")
        flag = True
        break
    elif guess < randomNum:
        print("You guessed too small, try again")
    elif guess > randomNum:
        print("You gussed too high, try again")
    

if not flag:
    print("You ran out of guesses, Game over!")