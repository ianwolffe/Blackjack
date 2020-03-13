import random   # Used to randomize cards chosen from cards_of_deck.

restart = True  # Will restart the program if the user wants to on lines 97-102.
while restart == True:
    # Deck of cards array, acts like a regular deck (when card is dealt out, it is removed from this array).
    cards_of_deck = ["Ad", "Ah", "Ac", "As", "2d", "2h", "2c", "2s", "3d", "3h", "3c", "3s",
        "4d", "4h", "4c", "4s", "5d", "5h", "5c", "5s", "6d", "6h", "6c", "6s", "7d", "7h",
        "7c", "7s", "8d", "8h", "8c", "8s", "9d", "9h", "9c", "9s", "10d", "10h", "10c", "10s",
        "Jd", "Jh", "Jc", "Js", "Qd", "Qh", "Qc", "Qs", "Kd", "Kh", "Kc", "Ks"]

    # Assigns each card a value according to the Blackjack rules.
    value_of_cards = {
        "Ah": 11, "Ad": 11, "As": 11, "Ac": 11, "2h": 2, "2d": 2, "2s": 2, "2c": 2, "3h": 3, "3d": 3, "3s": 3,
        "3c": 3, "4h": 4, "4d": 4, "4s": 4, "4c": 4, "5h": 5, "5d": 5, "5s": 5, "5c": 5, "6h": 6, "6d": 6,
        "6s": 6, "6c": 6, "7h": 7, "7d": 7, "7s": 7, "7c": 7, "8h": 8, "8d": 8, "8s": 8, "8c": 8, "9h": 9,
        "9d": 9, "9s": 9, "9c": 9, "10h": 10, "10d": 10, "10s": 10, "10c": 10, "Jh": 10, "Jd": 10, "Js": 10,
        "Jc": 10, "Qh": 10, "Qd": 10, "Qs": 10, "Qc": 10, "Kh": 10, "Kd": 10, "Ks": 10, "Kc": 10
    }

    # Deals two cards to the dealer, revealing one of them (hole card) to the player.
    n = random.choice(cards_of_deck)
    value_of_dealer = value_of_cards[n]
    print("Dealer's hole card: " + n)   # Reveals hole card to player.
    del n   # removes card from the deck.
    m = random.choice(cards_of_deck)
    value_of_dealer = value_of_dealer + value_of_cards[m]
    del m   # removes card from the deck.

    # Deals two cards to player, and reveals hand and value of hand.
    hand_of_player = ""
    i = random.choice(cards_of_deck)    # Random card from the deck.
    hand_of_player = hand_of_player + i
    value_of_hand = value_of_cards[i]   # Adds card value.
    del i
    j = random.choice(cards_of_deck)    # Second card from the deck.
    hand_of_player = hand_of_player + ", " + j
    value_of_hand = value_of_hand + value_of_cards[j]   # Adds value to first card.
    del j
    print("Your hand: " + hand_of_player + "\nTotal value of your hand: " + str(value_of_hand))

    bust = False   # Variable to determine if player busted used on lines 72-74.
    if value_of_hand != 21:
        print("Would you like to hit or stand?")
        response = input().lower()   # Takes an input from player if they have hand < 21.
    else:
        response = "stand"   # Automatically stands if player has hand = 21.

    if response == "hit":   # Player chooses to input "hit".
        while response == "hit":
            k = random.choice(cards_of_deck)   # Deals another card to the player.
            hand_of_player = hand_of_player + ", " + k
            # This for loop locates any ace cards that could potentially bust the player
            # if the value of the hand is greater than 21.
            for a in hand_of_player:
                if a == "A" and (value_of_hand + value_of_cards[k] > 21):
                    value_of_hand = value_of_hand - 10
            # Replace ace cards with "B" so the card is not iterated every time the player hits.
            hand_of_player = hand_of_player.replace("A", "B")
            value_of_hand = value_of_hand + value_of_cards[k]
            print(k + "\nTotal value of hand: " + str(value_of_hand))
            del k
            # Player doesn't bust or get Blackjack, so player can hit again if he/she chooses.
            if value_of_hand < 21:
                print("Would you like to hit or stand?")
                response = input()
                if response == "hit":
                    continue   # Player chooses to hit again, so loop reiterates.
                else:
                    pass   # Player stands, so loop ends.
            elif value_of_hand == 21:   # Player has blackjack, so loop breaks.
                break
            elif value_of_hand > 21:
                bust = True   # Player has busted, and loses as of lines 91-92.
                break

    if bust == False:   # Player did not bust, but might lose if dealer has better hand.
        # Standard Blackjack rules: dealer stands if hand is better than or equal to 17.
        # If dealer had equal hand to player, dealer wins.
        while value_of_dealer <= 16:
            q = random.choice(cards_of_deck)
            value_of_dealer = value_of_dealer + value_of_cards[q]
            del q
        if value_of_dealer > 21:    # Player wins because dealer busted.
            print("Dealer's hand was " + str(value_of_dealer) + " and busted. You win!")
        elif value_of_dealer >= value_of_hand:   # Player loses because dealer had better hand.
            print("Dealer's hand was " + str(value_of_dealer) + " and yours was " +
            str(value_of_hand) + ". You lose.")
        else:   # Player wins because dealer had worse hand.
            print("Dealer's hand was " + str(value_of_dealer) + " and yours was " +
            str(value_of_hand) + ". You win!")
    else:
        print("BUST. You lose.")    # Player busts and loses.

    # Restarts the program if the user wants to play again.
    print("Would you like to play again? (yes or no)")
    response = input()
    if response == "yes":
        pass
    else:
        restart = False