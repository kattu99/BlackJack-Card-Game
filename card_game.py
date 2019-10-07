import random
import time


num_decks = 5
deck = [x for x in range(2,15)]*4*num_decks  


def deal(deck):
    hand = []
    for i in range(2):
        random.shuffle(deck)
        card = deck.pop()
        if card == 11:
            hand.append("J")
        elif card == 12:
            hand.append("Q")
        elif card == 13:
            hand.append("K")
        else:
            hand.append(card)
    return hand

def hit(hand):
    card = deck.pop()
    if card == 11:
        card = "J"
    if card == 12:
        card = "Q"
    if card == 13:
        card = "K"
    if card == 14:
        card = "A"
    hand.append(card)
    return hand


def find_sum(hand):
    total = 0
    ace = 0
    for card in hand:
        if card == "J" or card == "Q" or card == "K":
            total += 10
        elif card == "A":
            ace += 1
        else:
            total += card
    for i in range(ace):
        if (total + 11 > 21):
            total += 1
        else:
            total += 11
    return total 


def result(dealer, player, pot, bet):
    dealer_result = find_sum(dealer)
    print("Dealer has: " + str(dealer_result))
    player_result = find_sum(player)
    print("Player has: " + str(player_result))
    if dealer_result == 21 and player_result == 21:
        print("TIE GAME, both are 21")
    elif dealer_result == 21:
        print("YOU LOSE, dealer got blackjack")
        pot -= bet 
        print("Your pot is " + str(pot))
    elif player_result == 21:
        pot += bet
        print("YOU WIN, blackjack")
        print("Your pot is " + str(pot))
    elif player_result < dealer_result:
        pot -= bet
        print("YOU LOST, dealer wins")
        print("Your pot is " + str(pot))
    elif dealer_result < player_result:
        pot += bet 
        print("YOU WIN")
        print("Your pot is " + str(pot))
    else:
        print("TIE")
    return pot


def play_again(pot):
    print("---------------------------------")
    once_more = raw_input("Do you want to play again (y/n)? ")
    if once_more == "y":
        [x for x in range(2,15)]*4*num_decks  
        game(pot)
    else:
        print("See ya next time")
        print("You finished with: "+str(pot)) 
        exit() 


def game(pot):
    deck = [x for x in range(2,15)]*4*num_decks  
    choice = 0
    bet = 0
    print("INTENSE BLACKJACK!\n")
    dealer = deal(deck)
    player = deal(deck)
    time.sleep(0.5)
    print("The dealer has " + str(dealer))
    print("It is worth " + str(find_sum(dealer)))
    time.sleep(0.5)
    print("---------------------------------")
    print("You're hand is " + str(player))
    print("It is worth " + str(find_sum(player)))
    print("---------------------------------")
    print("Your pot is " + str(pot))
    while True:
        try:
            bet = int(raw_input('Enter your bet: '))
            break
        except:
            print("That's not a valid option!")
    time.sleep(0.5)
    choice = raw_input("Do you want to [h]it, [s]tay, or [q]uit: ").lower()
    while True:
        if choice == "h":
            player = hit(player)
            print("You're hand is " + str(player))
            time.sleep(0.5)
            print("It is worth " + str(find_sum(player)))
            if find_sum(player) > 21:
                time.sleep(0.5)
                print("BUST. YOU LOSE")
                pot -= bet
                play_again(pot)
            print("---------------------------------")
        if choice == "s":
            while find_sum(dealer) <= 16:
                dealer = hit(dealer)
                time.sleep(0.5)
                print("The dealer now has " + str(dealer))
            if find_sum(dealer) > 21:
                print("YOU WIN. DEALER WENT BUST")
                pot += bet
                time.sleep(0.5)
                play_again(pot)
            else: 
                pot = result(dealer, player, pot, bet)
                play_again(pot)
            print("---------------------------------")
        elif choice == "q":
            print("See ya next time!")
            print("You finished with: "+str(pot)) 
            time.sleep(0.1)
            exit()
        choice = raw_input("Do you want to [h]it, [s]tay, or [q]uit: ").lower()

if __name__ == "__main__":
   game(0)
