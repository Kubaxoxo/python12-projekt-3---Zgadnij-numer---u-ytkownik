from ast import Expression
from distutils.command.install import HAS_USER_SITE
import numbers
import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random.number:
        guess = int(input('Odgadnij liczbę od 1 do: {x}'))
        print(guess)
        if guess < random_number:
            print('Pudło, zgadnij jeszcze raz. Za nisko.')
        elif guess > random_number:
            print('Pudło, zgadnij jeszcze raz. Za wysoko.')
    
    print(f'Gratulacje. Odgadłeś numer {random_number} prawidłowo!')

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Czy {guess} jest za wysokie (H), za niskie (L), lub prawidłowe (C)?? ').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    
    print(f'Tak! Komputer odgadł twój numer, {guess}, prawidłowo!')

computer_guess(10)