import random

# deck/player/dealer hand
deck = []
for x in range(2,11):
    for y in range(4):
        deck.append(x)

for x in ['A','J','Q','K']:
    for y in range(4):
        deck.append(x)
print(deck)

player_hand = []
dealer_hand = []

# deal the cards
def deal():
    player_hand.append(random.choices(deck, k=2))
    dealer_hand.append(random.choices(deck, k=2))

def hit(who):
    who.append(random.choice(deck))

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
        print(f'Hit!,{total(dealer_hand)}')
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