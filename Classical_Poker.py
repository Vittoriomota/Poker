
import random

test_hands = [
    # High Card
    ["2H", "4D", "7C", "9S", "KH"],
    # One Pair
    ["2H", "2D", "7C", "9S", "KH"],
    # Two Pair
    ["2H", "2D", "7C", "7S", "KH"],
    # Three of a Kind
    ["2H", "2D", "2C", "7S", "KH"],
    # Straight
    ["5H", "6D", "7C", "8S", "9H"],
    # Flush
    ["2H", "5H", "7H", "9H", "KH"],
    # Full House
    ["2H", "2D", "2C", "7S", "7H"],
    # Four of a Kind
    ["2H", "2D", "2C", "2S", "KH"],
    # Straight Flush
    ["5H", "6H", "7H", "8H", "9H"],
    # Royal Flush
    ["10H", "JH", "QH", "KH", "AH"]
]

rank_names = ["high card", "pair", "two pair", "three of a kind", "straight",
              "flush", "full house", "four of a kind", "straight flush"]

def suit(card):
    return card[-1]

def value(card):
    if card[0] == "A":
        return 14
    elif card[0] == "K":
        return 13
    elif card[0] == "Q":
        return 12
    elif card[0] == "J":
        return 11
    else:
        return int(card[0:-1])

def is_flush(cards):
    # ESTO ESTA MAL
    #first_suit = suit(cards[1])
    # for card in cards:
    #   if suit(card) != first_suit:
    #       return False
    #    else:
    #       return True
    return all([suit(card) == suit(cards[0]) for card in cards[1:-1]])

def hand_dist(cards):
    dist = {i: 0 for i in range(1, 15)}
    for card in cards:
        dist[value(card)] += 1
    dist[1] = dist[14]
    return dist

def straight_high_card(cards): #Entenderlo despues
    dist = hand_dist(cards)
    for value in range(1, 11):
        if all([dist[value + k] == 1 for k in range(5)]):
            return value + 4
    return None

#look for if there are any 3 of a kinds, 2 of a kinds, and return the number of the card

def card_count(cards, num, but=None):
    dist = hand_dist(cards)
    for value in range(2,15):
        if value == but:
            continue
        if (dist[value] == num):
            return value
    return None

def hand_rank(cards):
    if straight_high_card(cards) is not None and is_flush(cards):
        return 8
    if card_count(cards, 4) is not None:
        return 7
    if card_count(cards, 3) is not None and card_count(cards, 2) is not None:
        return 6
    if is_flush(cards):
        return 5
    if straight_high_card(cards) is not None:
        return 4
    if card_count(cards, 3) is not None:
        return 3
    pair1= card_count(cards, 2)
    if pair1 is not None:
        if card_count(cards, 2, but = pair1) is not None:
            return 2
        return 1
    return 0

def compare_hands(hand1, hand2):
    r1 = hand_rank(hand1)
    r2 = hand_rank(hand2)
    if r1 < r2:
        return -1
    if r1 > r2:
        return 1
    # need to add test for high cards - tie breakers
    else:
        return 0

def make_deck():
    deck = []
    for suit in ("D", "C", "H", "S"):
        for value in range(2,15):
            if value < 11:
                value_string = str(value)
            else:
                value_string = ("J", "Q", "K", "A")[value - 11]
            deck.append(value_string + suit)
    return deck

def shuffled_deck():
    deck = make_deck()
    random.shuffle(deck)
    return deck

def deal(deck, n):
    hand = deck[0:n]
    del deck[0:n]
    return hand

deck = shuffled_deck()

def show_compare_hands(hand1, hand2):
    sgn = compare_hands(hand1, hand2)
    result = ("loses to", "ties", "beats")[sgn+1]
    print(f"{hand1} {result} {hand2}")
    r1 = hand_rank(hand1)
    r2 = hand_rank(hand2)

def test_random_hands(n=20):
    for i in range(n):
        deck = shuffled_deck()
        show_compare_hands(deal(deck, 5), deal(deck, 5))

def rank_distribution(n=10000):
    dist = {i: 0 for i in range(9)}
    for i in range(n):
        deck = shuffled_deck()
        hand = deal(deck, 5)
        dist[hand_rank(hand)] += 1

    for r in range(9):
        print(f"{rank_names[r]}: {dist[r]} ({100 * dist[r] / n}%)")

print(rank_distribution(100000))




#for hand in test_hands:
    # print(hand)
    # print(hand_rank(hand))

#suit("AC")
#print(value("QC"))
