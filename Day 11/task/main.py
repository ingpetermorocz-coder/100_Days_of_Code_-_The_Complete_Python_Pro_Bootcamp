import art
import random

def score(hand, value):
    for card in hand:
        value += card
    if len(hand) == 0:
        value = "undefined"
    return value

def check_11(hand, value):
    if 11 in hand:
        number_of_aces = hand.count(11)
        for card in hand:
            value += card
        convert_aces = True
        while convert_aces:
            value -= 10
            number_of_aces -= 1
            if value <= 21:
                convert_aces = False
        return value
    else:
        return value

def current(pc, ps, cc):
    print(f"Your cards: {pc}, current score = {ps}.")
    print(f"Computer's first card: {cc[0]}.")

def final(pc, ps, cc, cs):
    print(f"Your final hand: {pc}, final score = {ps}.")
    print(f"Computer's final hand: {cc}, final score = {cs}.")

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
player_cards = []
computer_cards = []
play = True
while play:
    ask_for_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if ask_for_play == 'y':
        print("\n" * 50)
        print(art.logo)
        player_cards = [random.choice(deck), random.choice(deck)]
        computer_cards = [random.choice(deck), random.choice(deck)]
        player_score = score(hand=player_cards, value=0)
        computer_score = score(hand=computer_cards, value=0)
        if player_score == 22:
            player_score = 12
            current(pc=player_cards, ps=player_score, cc=computer_cards)
        else:
            current(pc=player_cards, ps=player_score, cc=computer_cards)
        if player_score == 21:
            while computer_score < 17:
                computer_cards.append(random.choice(deck))
                computer_score = score(hand=computer_cards, value=0)
                if computer_score > 21:
                    computer_score = check_11(hand=computer_cards, value=computer_score)
            final(pc=player_cards, ps=player_score, cc=computer_cards, cs=computer_score)
            if player_score == computer_score:
                print("Draw. \U0001F643")
            else:
                print("You win with Blackjack! \U0001F60E")
        else:
            get_card = True
            while get_card:
                decision = input("Type 'y' to get another card, type 'n' to pass: ")
                if decision == "y":
                    player_cards.append(random.choice(deck))
                    player_score = score(hand=player_cards, value=0)
                    if player_score > 21:
                        player_score = check_11(hand=player_cards, value=player_score)
                        if player_score > 21:
                            final(pc=player_cards, ps=player_score, cc=computer_cards, cs=computer_score)
                            print("You went over. \U00002757 You lose. \U0001F627")
                            get_card = False
                        elif player_score == 21:
                            while computer_score < 17:
                                computer_cards.append(random.choice(deck))
                                computer_score = score(hand=computer_cards, value=0)
                                if computer_score > 21:
                                    computer_score = check_11(hand=computer_cards, value=computer_score)
                            final(pc=player_cards, ps=player_score, cc=computer_cards, cs=computer_score)
                            if computer_score == 21:
                                print("Draw. \U0001F643")
                            else:
                                print("You win with Blackjack! \U0001F60E")
                            get_card = False
                        else:
                            current(pc=player_cards, ps=player_score, cc=computer_cards)
                            get_card = True
                    elif player_score == 21:
                        while computer_score < 17:
                            computer_cards.append(random.choice(deck))
                            computer_score = score(hand=computer_cards, value=0)
                            if computer_score > 21:
                                computer_score = check_11(hand=computer_cards, value=computer_score)
                        final(pc=player_cards, ps=player_score, cc=computer_cards, cs=computer_score)
                        if computer_score == 21:
                            print("Draw. \U0001F643")
                        else:
                            print("You win with Blackjack! \U0001F60E")
                        get_card = False
                    else:
                        current(pc=player_cards, ps=player_score, cc=computer_cards)
                        get_card = True
                else:
                    while computer_score < 17:
                        computer_cards.append(random.choice(deck))
                        computer_score = score(hand=computer_cards, value=0)
                        if computer_score > 21:
                            computer_score = check_11(hand=computer_cards, value=computer_score)
                    final(pc=player_cards, ps=player_score, cc=computer_cards, cs=computer_score)
                    if computer_score > 21:
                        print("Computer went over. \U0001F440 You win. \U0001F600")
                    elif computer_score == 21:
                        print("Computer wins with Blackjack. \U0001F920 You lose. \U0001F62F")
                    elif player_score < computer_score:
                        print("You lose. \U0001F62D")
                    elif player_score == computer_score:
                        print("Draw. \U0001F643")
                    else:
                        print("You win. \U0001F642")
                    get_card = False
    elif ask_for_play == 'n':
        play = False
    else:
        player_score = score(hand=player_cards, value=0)
        computer_score = score(hand=computer_cards, value=0)
        final(pc=player_cards, ps=player_score, cc=computer_cards, cs=computer_score)
        print("Draw. \U0001F643")
