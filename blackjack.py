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
    pass

def check_winner():
    pass


# Game loop
def play():
    hit(player_hand, 2)
    hit(dealer_hand, 2)
    
    print(f'Dealer Hand:{dealer_hand[0]}, ?')
    time.sleep(2)
    print(f'Your Hand:{player_hand}')
    print(f'Total:{total(player_hand)}')

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
                return
        elif next_move == '2':
            hit_cycle = False
        else:
            print('Invalid Input.')
    
    print(f'Dealer Hand:{dealer_hand}')
    print(f'Total:{total(dealer_hand)}')

    # Dealer Hit Cycle
    while total(dealer_hand) < 17:
        hit(dealer_hand, 1)
        print('Dealer Hit!')
        print(f'Dealer Hand:{dealer_hand}')
        print(f'Total:{total(dealer_hand)}')
        time.sleep(2)
        if total(dealer_hand) > 21:
            print('Dealer Busted!\nYou Win')
            return

    if total(player_hand) > total(dealer_hand):
        print('You Win!')
        return
    elif total(player_hand) == total(dealer_hand):
        print('Tie!')
        return
    else:
        print('You Lose!')
        return
play()

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