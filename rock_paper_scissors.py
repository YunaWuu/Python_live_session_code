# rock paper scissors game
import random
choices = ['r', 'p', 's']
user = input('Enter "r", "p", or "s": ').lower()
while user in choices:
    computer = choices[random.randint(0,2)]
    print('User:', user)
    print('Computer:', computer)
    if user == 'r' and computer == 'p':
        print('Computer Wins!')
    elif user == 'r' and computer == 's':
        print('You Win!')
    elif user == 'p' and computer == 's':
        print('Computer Wins!')
    elif user == 'p' and computer == 'r':
        print('You Win!')
    elif user == 's' and computer == 'r':
        print('Computer Wins!')
    elif user == 's' and computer == 'p':
        print('You Win!')
    else:
        print('Draw!')
    user = input('Enter "r", "p", or "s": ').lower()
