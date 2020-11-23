'''
Games
'''
import random

def guess_the_number():
    '''Guess the number game'''
    work_on = True
    while work_on:
        print("***** WELCOME TO GUESS THE NUMBER GAME! *****")
        random_number = random.randint(1,100)
        live = int(input(' Enter lives :'))
        count_live = live
        count = 0

        while count_live > 0:
            count_live = count_live - 1
            count = count + 1
            given_number = int(input(' Enter a number : '))

            if given_number > random_number:
                print('Lower ')

            elif given_number == random_number:
                print(f'You found it ! {count} times tried. Total points : {100 - (100/live) * (count - 1)}')
                break

            else:
                print('Upper ')

            if count_live == 0:
                print(f'Out of lives. Number : {random_number}. Points : {0}')

        print("\n1- Play Again\n00- EXIT to Games Menu\n99- EXIT")
        ask = input("Enter choice :")
        if ask == "1":
            guess_the_number()
        elif ask == "00":
            break
        elif ask == "99":
            raise SystemExit
        else:
            continue

def negative_index():
    '''Negative indexing game'''
    work_on = True
    while work_on:
        program_on = True
        while program_on:
            print("***** WELCOME TO NEGATIVE INDEX GAME! *****")
            word = input("Enter whatever you want to reverse it ! : ")
            print(word[::-1])
            if word == word[::-1]:
                print("It's a palindrome !")
                break
            break
        print("\n1- Play Again\n00- EXIT to Games Menu\n99- EXIT")
        ask = input("Enter choice :")
        if ask == "1":
            negative_index()
        elif ask == "00":
            break
        elif ask == "99":
            raise SystemExit
        else:
            continue
