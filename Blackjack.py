import random

# Setting Default Decks/Values
dealer = []
dealer_hidden = []
user = []
user_value = 0
dealer_value = 0

# Generating Range of 52 Numbers
deck = list(range(1, 52))

# Creating Deck of Cards
num_icon = {1: (11, 'Hearts'), 2: (11, 'Diamonds'), 3: (11, 'Clubs'), 4: (11, 'Spades'),  # Ace
            5: (2, 'Hearts'), 6: (2, 'Diamonds'), 7: (2, 'Clubs'), 8: (2, 'Spades'),  # 2
            9: (3, 'Hearts'), 10: (3, 'Diamonds'), 11: (3, 'Clubs'), 12: (3, 'Spades'),  # 3
            13: (4, 'Hearts'), 14: (4, 'Diamonds'), 15: (4, 'Clubs'), 16: (4, 'Spades'),  # 4
            17: (5, 'Hearts'), 18: (5, 'Diamonds'), 19: (5, 'Clubs'), 20: (5, 'Spades'),  # 5
            21: (6, 'Hearts'), 22: (6, 'Diamonds'), 23: (6, 'Clubs'), 24: (6, 'Spades'),  # 6
            25: (7, 'Hearts'), 26: (7, 'Diamonds'), 27: (7, 'Clubs'), 28: (7, 'Spades'),  # 7
            29: (8, 'Hearts'), 30: (8, 'Diamonds'), 31: (8, 'Clubs'), 32: (8, 'Spades'),  # 8
            33: (9, 'Hearts'), 34: (9, 'Diamonds'), 35: (9, 'Clubs'), 36: (9, 'Spades'),  # 9
            37: (10, 'Hearts'), 38: (10, 'Diamonds'), 39: (10, 'Clubs'), 40: (10, 'Spades'),  # 10
            41: (10, 'Hearts'), 42: (10, 'Diamonds'), 43: (10, 'Clubs'), 44: (10, 'Spades'),  # Jack
            45: (10, 'Hearts'), 46: (10, 'Diamonds'), 47: (10, 'Clubs'), 48: (10, 'Spades'),  # Queen
            49: (10, 'Hearts'), 50: (10, 'Diamonds'), 51: (10, 'Clubs'), 52: (10, 'Spades')  # King
            }

# Generating Random 1-52 Index to Choose Card Number and Icon
def draw_card():
    output = random.choice(deck) # Generate Random Output
    deck.remove(output) # Removing Card from Deck
    num = num_icon[output][0] # Card Number
    icon = num_icon[output][1] # Card Icon
    return [num, icon]

# Initiate Game
def start_game():
    cont = 0 #Starting Value for While Loop
    while cont == 0:
        start = input("Draw Card? (y/n): ")
        print() #Spacing
        if start == 'y' or start == 'Y': #Drawing card for dealer and user
            play_first_round()
            cont = 1 #Stop While Loop
        elif start == 'n' or start == 'N': #Folding
            cont = 1
        else: #If User Enters Invalid Response
            print('Enter \'y\' to Draw Card or \'n\' to Fold...')

# Organizing First Round
def play_first_round():
    global user_value, dealer_value
    # Draw first cards
    user_card = draw_card()
    user.append(user_card) #Upload Card to User Deck
    user_value += user_card[0]
    dealer_card = draw_card()
    dealer.append(dealer_card) #Upload Card to Dealer Deck
    dealer_value += dealer_card[0]
    # Draw second card
    user_card = draw_card()
    user.append(user_card)
    user_value += user_card[0]
    # Revealing Cards
    print('Dealer\'s Deck   =    {}'.format(dealer))
    print('Dealer\'s Value  =    {}'.format(dealer_value))
    print('Your Deck       =    {}'.format(user))
    print('Your Value      =    {}'.format(user_value), end='\n'*2)
    # Hidden Dealer 2nd Card
    dealer_hidden_card = draw_card()
    dealer_hidden.append(dealer_hidden_card)
    if user_value == 21: #Checking for Blackjack to Jump to Dealer Round
        print('BLACKJACK!')
        dealer_round()
    # Draw or Fold
    cont2 = 0 #Starting Value for While Loop
    while cont2 == 0:
        draw_fold = input("Draw Another Card? (y/n): ")
        if draw_fold == 'y' or draw_fold == 'Y':
            play_next_round()
            cont2 = 1 #Stop While Loop
        elif draw_fold == 'n' or draw_fold == 'N':  #Fold and Jump to Dealer Round
            dealer_round()
        else:
            print('Enter \'y\' to Draw Card or \'n\' to Fold...')

# Next User Rounds
def play_next_round():
    card_reveal()
    cont3 = 0 #Starting Value for While Loop
    while cont3 == 0:
        draw_fold = input("Draw Another Card? (y/n): ")
        print() #Spacing
        if draw_fold == 'y' or draw_fold == 'Y':
            card_reveal()
        elif draw_fold == 'n' or draw_fold == 'N':
            dealer_round()
            cont3 = 1
        else:
            print('Enter \'y\' to Draw Card or \'n\' to Fold...')

# Revealing User Rounds
def card_reveal():
    global user_value, dealer_value
    # Draw user card
    user_card = draw_card()
    user.append(user_card)
    user_value += user_card[0]
    # Check for Aces and Change Value if Necessary
    for card in user:
        if card[0] == 11 and user_value > 21:
            card[0] = 1
            user_value -= 10
    # Card Reveal
    print('Dealer\'s Deck   =    {}'.format(dealer))
    print('Dealer\'s Value  =    {}'.format(dealer_value))
    print('Your Deck       =    {}'.format(user))
    print('Your Value      =    {}'.format(user_value), end='\n'*2)
    if user_value > 21:
        print('BUST!', end='\n'*2)
        dealer_round()
    if user_value == 21:
        print('BLACKJACK!', end='\n'*2)
        dealer_round()

# Final Dealer Rounds
def dealer_round():
    global user_value, dealer_value
    # Getting Dealer 2nd Card
    print('Starting Dealer Round...', end='\n'*2)
    input("Click Enter to Reveal Hidden Dealer Card...")
    print() #Spacing
    dealer.append(dealer_hidden)
    dealer_value += dealer_hidden[0][0]
    print('Dealer\'s Deck   =    {}'.format(dealer))
    print('Dealer\'s Value  =    {}'.format(dealer_value))
    print('Your Deck       =    {}'.format(user))
    print('Your Value      =    {}'.format(user_value), end='\n'*2)
    # Checking to See if Dealer < 17 (House Rules)
    while dealer_value < 17:
        input("Click Enter to Initiate Next Dealer Draw...")
        print() #Spacing
        dealer_card = draw_card()
        # Check for Aces and Change Value if Necessary
        for card in dealer:
            if card[0] == 11 and dealer_value > 21:
                card[0] = 1
                dealer_value -= 10
        dealer.append(dealer_card)
        dealer_value += dealer_card[0]
        print('Dealer\'s Deck   =    {}'.format(dealer))
        print('Dealer\'s Value  =    {}'.format(dealer_value))
        print('Your Deck       =    {}'.format(user))
        print('Your Value      =    {}'.format(user_value), end='\n'*2)
    # Final Outcome
    if dealer_value <= 21:
        if dealer_value == user_value: #Both Hit Jackpot or Equal Value
            print('TIE')
        elif user_value > 21: #User Bust
            print('DEALER WINS')
        elif dealer_value > user_value: #Dealer Higher Value
            print('DEALER WINS')
        else: #User Higher Value and Less Than 21
            print('YOU WON!')
    else:
        if user_value > 21: #Both Bust
            print("DEALER BUST", end='\n'*2)
            print('TIE')
        else: #Dealer Bust
            print("DEALER BUST", end='\n' * 2)
            print('YOU WON!')
    quit()


start_game()
