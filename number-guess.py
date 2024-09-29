import random
import time

number = random.randint(0,100)
print("GUESS THE NUMBER:")
guess = int(input("Enter your guess:- "))
if (guess == number):
    print("You got it correct! Congrats!")
    time.sleep(1)
    print("The number was", number)

elif (guess < 100):
    print("The numbers are between 1 to 100.")
    time.sleep(1)
    print("The number was", number)

else:
    print("Sorry, you were wrong.")
    time.sleep(1)
    print("The number was", number)