import random
import time 
from unittest.mock import MagicMock

switch = True

# deck/player/dealer hand
deck = []
for x in range(2,11):
    for y in range(4):
        deck.append(x)

for x in ['A','J','Q','K']:
    for y in range(4):
        deck.append(x)

player_hand = []
dealer_hand = []

# deal the cards

def hit(who, times):

    for _ in range(times):
        card = random.choice(deck)
        deck.remove(card)
        who.append(card)
    

# calculate the total of each hand
def total(who):
    total = 0
    for x in who:
        if type(x) == int:
            total += x
        elif x in "JQK":
            total += 10
        else:
            if total < 11:
                total += 11
            else:
                total += 1
    return total

# check for the winner

def check(dealer=False):
    if dealer:
        if total(dealer_hand) > 21:
            print('Dealer Busted, You Win!')
            return
    if total(player_hand) > 21:
            print('You Busted!, Dealer Win.')
            return
    if total(player_hand) == 21:
        if total(dealer_hand) == 21:
            print(f'Dealer Hand:{dealer_hand}')
            print('BlackJack Tie!')
            return 
        print('BlackJack!, You Win!')
        return 


def show_hand(dealer=False,hide=False):
    if dealer:
        if hide:
            print(f'Dealer Hand:{dealer_hand[0]}, ?')
            return 
        print(f'Dealer Hand:{dealer_hand} Total:{total(dealer_hand)}')
    else:
        print(f'Your Hand:{player_hand} Total:{total(player_hand)}')


# Game loop
def play():
    hit(player_hand, 2)
    hit(dealer_hand, 2)
    
    show_hand(dealer=True,hide=True)
    time.sleep(2)
    show_hand()

    #BlackJack
    if total(player_hand) == 21:
        if total(dealer_hand) == 21:
            print(f'Dealer Hand:{dealer_hand}')
            print('BlackJack Tie!')
            return 
        print('BlackJack!, You Win!')
        return 

    hit_cycle = True

    #Player hit cycle
    while hit_cycle:
        next_move = input('1: Hit\n2: Stay\n')
        if next_move == '1':
            hit(player_hand, 1)

            show_hand()

            # Check
            if total(player_hand) > 21:
                print('You Busted!, Dealer wins.')
                return
        elif next_move == '2':
            hit_cycle = False
        else:
            print('Invalid Input.')
    
    show_hand(dealer=True)

    # Dealer Hit Cycle
    while total(dealer_hand) < 17:
        hit(dealer_hand, 1)
        print('Dealer Hit!')
        show_hand(dealer=True)
        time.sleep(2)
        if total(dealer_hand) > 21:
            print('Dealer Busted, You Win!')
            return

    if total(player_hand) > total(dealer_hand):
        print('You Win!')
        return
    elif total(player_hand) == total(dealer_hand):
        print('Tie!')
        return
    else:
        print('Dealer Wins.')
        return

#play()
'''
CodeCoach

for _ in range(2):
    dealCard(dealerHand)
    dealCard(playerHand)

while playerIn or dealerIn:
    print(f'{dealer_hand}')
    print(f'player_hand')   
    if playerIn:
        stayOrHit = input('1:Hit/n2:Stay')
    if total(dealerHand) > 16:
        dealerIn = False
    else:
        dealCard(dealerHand)
    if stayOrHit == '2':
        playerIn = False
    if total(playerHand) >= 21:
        break
    elif total(dealerHand) >= 21:
        break

if ....

'''