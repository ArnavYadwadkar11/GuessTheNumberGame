import random
import colorama
from colorama import Fore
SecretNumber = random.randrange(start=1, stop=35)
print(Fore.MAGENTA + 'Guess the randomly generated number from 1 to 35')
chances = 1
guess = None
while guess != SecretNumber :
    guess = ((int(input("Guess a number between 1 and 35: "))))
    if guess > SecretNumber:
        print(Fore.RED + 'Guess Lower!')
        chances +=1
    elif guess < SecretNumber:
            print(Fore.GREEN + 'Guess Higher!')
            chances +=1
    elif guess == SecretNumber:
            print(Fore.YELLOW + 'Hurray! You got it in {} tries, the number was {}'.format(chances, SecretNumber))