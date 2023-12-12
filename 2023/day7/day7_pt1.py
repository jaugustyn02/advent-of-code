from collections import defaultdict
from enum import Enum



# input = 'data/sample.txt'
input = 'data/puzzle.txt'


# poker_hands = Enum('poker_hands', ['FIVE', 'FOUR', 'FULL', 'THREE', 'TWO_PAIR', 'PAIR', 'HIGH'])
# poker_hands = (Enum('poker_hands', ['HIGH', 'PAIR', 'TWO_PAIR', 'THREE', 'FULL', 'FOUR', 'FIVE']))
class poker_hands(Enum):
    HIGH = 'a'
    PAIR = 'b'
    TWO_PAIR = 'c'
    THREE = 'd'
    FULL = 'e'
    FOUR = 'f'
    FIVE = 'g'

# char_map = Enum('figures', ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2', '1'])

char_map = {'A': 14, 'K': 13, 'Q': 12, 'J': 11, 'T': 10, '9': 9, '8': 8, '7': 7, '6': 6, '5': 5, '4': 4, '3': 3, '2': 2, 'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6}

def hand_radix_sort(hands_and_bets):
    n = len(hands_and_bets)
    m = len(char_map)
    str_len = len(hands_and_bets[0][0])
    for i in range(str_len-1, -1, -1):
        count = [0] * m
        output = [0] * n
        for j in range(n):
            count[char_map[hands_and_bets[j][0][i]]] += 1
        for j in range(1, m):
            count[j] += count[j-1]
        for j in range(n-1, -1, -1):
            output[count[char_map[hands_and_bets[j][0][i]]]-1] = hands_and_bets[j]
            count[char_map[hands_and_bets[j][0][i]]] -= 1
        hands_and_bets = output
    return hands_and_bets


def main():
    with open(input, 'r') as f:
        lines = f.readlines()
        hands_and_bids = []
        for line in lines:
            hand, bid = line.strip().split()
            # print(hand, bet)
            cards = defaultdict(int)
            for card in hand:
                cards[card] += 1
            
            # print(cards.items())
            sorted_hand = sorted(cards.items(), key=lambda x: x[1], reverse=True)
            if sorted_hand[0][1] == 5:
                val = poker_hands.FIVE.value
            elif sorted_hand[0][1] == 4:
                val = poker_hands.FOUR.value
            elif sorted_hand[0][1] == 3 and sorted_hand[1][1] == 2:
                val = poker_hands.FULL.value
            elif sorted_hand[0][1] == 3:
                val = poker_hands.THREE.value
            elif sorted_hand[0][1] == 2 and sorted_hand[1][1] == 2:
                val = poker_hands.TWO_PAIR.value
            elif sorted_hand[0][1] == 2:
                val = poker_hands.PAIR.value
            else:
                val = poker_hands.HIGH.value
            
            hands_and_bids.append((str(val)+hand, bid))

        sum = 0
        for rank, (_, bid) in enumerate(hand_radix_sort(hands_and_bids)):
            # print(rank+1, bid, _)
            sum += int(bid)*(rank+1)
        print(sum)

if __name__ == '__main__':
    main()