import random
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


def show_hand():
    print(f'Dealer Hand:{dealer_hand[0]}, ?')
    print(f'Your Hand:{player_hand}')
    print(f'total:{total(player_hand)}')


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

def check_before_reveal():
    if total(player_hand) > 21:
        print('You Busted!')
        return

def check_winner():
    # BLack Jacks
    if total(player_hand) == 21:
        if total(dealer_hand) == 21:
            print('BlackJack Tie!')
            return
        else:
            print('BlackJack, You Win!')
            return

    # Dealer have to hit
    while total(dealer_hand) < 17:
        hit(dealer_hand)
        print(f'Dealer Hit!,{total(dealer_hand)}')
        if total(dealer_hand) > 21:
            print('Dealer Busted!\nYou Win')

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
    show_hand()
    switch = False
