import random
import time 

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

def check():
    if total(player_hand) > 21:
        print('You Busted!')
        switch = False
    return

def check_winner():
    # BLack Jacks
    if total(player_hand) == 21:
        if total(dealer_hand) == 21:
            print('BlackJack Tie!')
            switch = False
        else:
            print('BlackJack, You Win!')
            switch = False

    # Dealer have to hit


    # Tied game
    if total(player_hand) == total(dealer_hand):
        print('Tie!')
        return

    #Player win
    if player_hand > dealer_hand and player_hand < 22:
        print(f'You win!')


# game loop
while switch:
    hit(player_hand, 2)
    hit(dealer_hand, 2)
    
    print(f'Dealer Hand:{dealer_hand[0]}, ?')
    time.sleep(2)
    print(f'Your Hand:{player_hand}')
    print(f'Total:{total(player_hand)}')

    hit_cycle = True

    while hit_cycle:
        time.sleep(2)
        next_move = input('1: Hit\n2: Stay\n')
        if next_move == '1':
            hit(player_hand, 1)

            # Show Hand
            print(f'Your Hand:{player_hand}')
            print(f'Total:{total(player_hand)}')

            # Check
            if total(player_hand) > 21:
                print('You Busted')
                switch = False
        elif next_move == '2':
            hit_cycle = False
        else:
            print('Invalid Input.')
    
    print(f'Dealer Hand:{dealer_hand}')
    print(f'Total:{total(dealer_hand)}')

    while total(dealer_hand) < 17:
        hit(dealer_hand, 1)
        print('Dealer Hit!')
        print(f'Dealer Hand:{dealer_hand}')
        print(f'Total:{total(dealer_hand)}')
        time.sleep(2)
        if total(dealer_hand) > 21:
            print('Dealer Busted!\nYou Win')
            switch = False

    if total(player_hand) > total(dealer_hand):
        print('You Win!')
        switch = False
    elif total(player_hand) == total(dealer_hand):
        print('Tie!')
        switch = False
    else:
        print('You Lose!')
        switch = False

