import random
secret_number = random.randint(1,100)
print('Welcome to secret number guessing game  ')
print('I am thinking of a number between 1 and 100 , can you guess it?')
while True:
        guess =int(input('Enter your guess: '))
        if guess < 1 or guess > 100:
         print("Pick a number between 1 and 100!")
        elif guess < secret_number:
         print('Your guess is too low! Try again.')
        elif guess > secret_number:
         print('Your guess is too high! Try again.')
        else:
         print( f"You guessed correctly! the number was {secret_number}. ")
         break

