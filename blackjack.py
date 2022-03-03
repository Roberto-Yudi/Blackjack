import random
import time

# Helper functions


def hit(who, times):
    for _ in range(times):
        card = random.choice(deck)
        deck.remove(card)
        who.append(card)


def total(who):
    total = 0
    for x in who:
        if isinstance(x, int):
            total += x
        elif x in "JQK":
            total += 10
        else:
            if total < 11:
                total += 11
            else:
                total += 1
    return total


def show_hand(dealer=False, hide=False):
    if dealer:
        if hide:
            print(f'Dealer Hand:{dealer_hand[0]}, ?')
            return
        print(f'Dealer Hand:{dealer_hand} Total:{total(dealer_hand)}')
    else:
        print(f'Your Hand:{player_hand} Total:{total(player_hand)}')


def generate_deck():
    deck = []
    for x in range(2, 11):
        for _ in range(4):
            deck.append(x)

    for x in ['A', 'J', 'Q', 'K']:
        for _ in range(4):
            deck.append(x)
    return deck


player_credits = 100
bet = 0

# Game loop
while player_credits > 0:
    deck = generate_deck()

    player_hand = []
    dealer_hand = []

    def play():
        global player_credits
        print(f'You have {player_credits} points')

        # Deal
        hit(player_hand, 2)
        hit(dealer_hand, 2)

        # Bet
        while True:
            try:
                bet = float(input("Place your bet\n"))
                if bet <= 0:
                    print('You can\'t bet nothing.🙃')
                elif bet > player_credits:
                    print('You don\'t have enough credits.😐')
                else:
                    break
            except ValueError:
                print('Invalid input.🚫')

        show_hand(dealer=True, hide=True)
        time.sleep(2)
        show_hand()

        # BlackJack
        if total(player_hand) == 21:
            if total(dealer_hand) == 21:
                print(f'Dealer Hand:{dealer_hand}')
                print('BlackJack Tie!🤯')
                return
            print('---- ♠BlackJack!, You Win!🍀 ----')
            print(f'You earned: {bet * 1.5}')
            player_credits += bet * 1.5

            return

        # Double Down
        if total(player_hand) in range(9, 12):
            while True:
                print('Double Down?🤑')
                double = input('1:yes \n2:no\n')
                if double == '1':
                    if player_credits < bet:
                        print('You dont have enough credits.😮')
                        break
                    else:
                        player_credits -= bet
                        print('You doubled your bet.🤪')
                        hit(player_hand, 1)
                        time.sleep(2)
                        show_hand()

                        # Final Check
                        if total(player_hand) > 21:
                            print('----You Busted on a 2x bet!, Dealer wins.😭 ----')
                            player_credits -= bet * 2
                            return
                        elif total(player_hand) > total(dealer_hand):
                            show_hand(dealer=True)
                            print('----You won a 2x bet!😎 ----')
                            player_credits += bet * 2
                            return
                        elif total(player_hand) == total(dealer_hand):
                            print('----Tie!😐----')
                            return
                        else:
                            show_hand(dealer=True)
                            print('----Dealer won a 2x bet.😰 ----')
                            player_credits -= bet * 2
                            return

                elif double == '2':
                    break
                else:
                    print('Invalid input.🚫')

        # Player hit cycle
        while True:
            next_move = input('🤔\n1: Hit\n2: Stay\n')
            if next_move == '1':
                hit(player_hand, 1)

                show_hand()

                # Bust Check
                if total(player_hand) > 21:
                    print('----You Busted!, Dealer wins.😒 ----')
                    player_credits -= bet
                    return
            elif next_move == '2':
                break
            else:
                print('Invalid Input.🚫')

        show_hand(dealer=True)

        # Dealer Hit Cycle
        while total(dealer_hand) < 17:
            hit(dealer_hand, 1)
            print('Dealer Hit!')
            show_hand(dealer=True)
            time.sleep(2)

            # Bust Check
            if total(dealer_hand) > 21:
                print('----Dealer Busted, You Win!😂 ----')
                print(f'You earned: {bet}')
                player_credits += bet

                return
        # Final Check
        if total(player_hand) > total(dealer_hand):
            time.sleep(2)
            print('----You have the best hand!, You Win.😁 ----')
            print(f'You earned: {bet}')
            player_credits += bet

            return
        elif total(player_hand) == total(dealer_hand):
            time.sleep(2)
            print('----It\'s a Tie!🤷----')
            return
        else:
            time.sleep(2)
            print('----Dealer have the best hand, Dealer Wins.😥 ----')
            player_credits -= bet
            return
    play()
