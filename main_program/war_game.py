'''
THIS IS THE WAR GAME.
'''
import random
suits = ("Hearts", "Spades", "Diamonds", "Clubs")
ranks = ("Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace")
values = {"Two":2, "Three":3, "Four":4, "Five":5,
          "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10,
          "Jack":11, "Queen":12, "King":13, "Ace":14}

class Cards:
    '''
    Cards class to hold card suit-rank
    '''
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.suit + " of " + self.rank

class Deck:
    '''
    DECKS CLASS FOR HOLDING THE CARDS ON HAND OF EACH PLAYER
    '''
    def __init__(self):
        # Note this only happens once upon creation of a new Deck
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Cards(suit, rank))

    def shuffle(self):
        '''
        SHUFFLES THE CARDS
        '''
        random.shuffle(self.all_cards)

    def deal_one(self):
        '''
        DEALS ONE CARD
        '''
        return self.all_cards.pop()

class Player():
    '''
    PLAYERS CLASS
    '''
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        '''
        REMOVES A CARD
        '''
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        '''
        ALL CARDS
        '''
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'

player_one = Player("One")
player_two = Player("Two")

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

ROUND_NUM = 0
GAME_ON = True
while GAME_ON:
    ROUND_NUM += 1
    print(f"Round {ROUND_NUM}")

    if len(player_one.all_cards) == 0:
        print("Player 1 is out of cards. Player two wins ! ")
        GAME_ON = False
        break
    elif len(player_two.all_cards) == 0:
        print("Player 2 is out of cards. Player one wins ! ")
        GAME_ON = False
        break

    #Start a new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    AT_WAR = True

    while AT_WAR:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)
            AT_WAR = False

        elif player_two_cards[-1].value > player_one_cards[-1].value:
            player_two.add_cards(player_two_cards)
            player_two.add_cards(player_one_cards)
            AT_WAR = False
        else:
            print("WAR ! ")
            if len(player_one.all_cards) < 5:
                print("Player 1 unable to declare a war !")
                print("Player 2 WINS ! ")
                GAME_ON = False
                break
            elif len(player_two.all_cards) < 5:
                print("Player 2 unable to declare a war !")
                print("Player 1 WINS ! ")
                GAME_ON = False
                break
            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
