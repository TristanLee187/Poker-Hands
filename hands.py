# make random 5 card poker hands and stop when a 5-card combo is obtained.

from random import sample
from collections import Counter
from time import sleep

ranks = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
suits = ['\u2666', '\u2663', '\u2665', '\u2660']
deck = []
for rank in ranks:
    for suit in suits:
        deck.append((rank, suit))


def gen_hand():
    hand = sample(deck, 5)
    card_comp = lambda card: (ranks.index(card[0]), suits.index(card[1]))
    hand.sort(key=card_comp)
    return hand


def is_straight(hand):
    return all([ranks.index(hand[i][0]) - ranks.index(hand[i - 1][0]) == 1 for i in range(1, 5)]) \
           or [hand[i][0] for i in range(5)] == ['A', '2', '3', '4', '5']


def is_flush(hand):
    return all([hand[i][1] == hand[i - 1][1] for i in range(1, 5)])


def is_straight_flush(hand):
    return is_flush(hand) and is_straight(hand)


def is_royal_flush(hand):
    return is_straight_flush(hand) and 'A' in [hand[i][0] for i in range(5)]


def is_full_house(hand):
    counts = Counter([hand[i][0] for i in range(5)])
    return sorted(list(counts.values())) == [2, 3]


def is_quads(hand):
    counts = Counter([hand[i][0] for i in range(5)])
    return 4 in counts.values()


combos = [is_royal_flush, is_straight_flush, is_quads, is_full_house, is_flush, is_straight]
combo_names = ['Royal Flush', 'Straight Flush', 'Quads', 'Full House', 'Flush', 'Straight']


def main():
    c = 0
    while True:
        c += 1
        h = gen_hand()
        print('Hand {}:'.format(c))
        hand_string = ', '.join([card[0]+card[1] for card in h])
        print(hand_string)
        for i in range(len(combos)):
            if combos[i](h):
                # print(*h)
                if i == 2:
                    print('It\'s Quads!')
                else:
                    print('It\'s a {}!'.format(combo_names[i]))
                return
        sleep(1)


if __name__ == '__main__':
    main()
