def guess_the_number():
    import random
    print("***** WELCOME TO GUESS THE NUMBER GAME! *****")
    r = random.randint(1,100)
    can = int(input(' Enter lives :'))
    hak = can
    sayac = 0 

    while hak>0:
        hak = hak - 1
        sayac = sayac + 1 
        x = int(input(' Enter a number : '))
        
        if x == r:
            print(f'You found it ! . {sayac}. times tried. Total points : {100 - (100/can) * (sayac - 1) }')
            break
        elif x>r:
            print('Lower ')
            
        elif x<r:
            print('Upper ')
        if hak == 0:
            print(f'Out of lives. Number : {r}. Points : {0}')

def negative_index():
    print("***** WELCOME TO NEGATIVE INDEX GAME! *****")
    negative = input("Enter whatever you want to reverse it ! : ")
    print(negative[::-1])