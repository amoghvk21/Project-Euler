from copy import deepcopy


VALUES = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

def royalFlushOld(h):
    string = ' '.join(list(h))

    if "K" in string:
        suit = string[string.index("K")+1]
    else:
        return False
    
    if (set([f"T{suit}"]).issubset(h)) and (set([f"J{suit}"]).issubset(h)) and (set([f"Q{suit}"]).issubset(h)) and (set([f"K{suit}"]).issubset(h)) and (set([f"A{suit}"]).issubset(h)):
        return True
    else:
        return False


def royalFlush(h):
    if straightFlush(h):
        s = ' '.join(list(h))
        return ((s.count("T") == 1) and (s.count("J") == 1) and (s.count("Q") == 1) and (s.count("K") == 1) and (s.count("A") == 1))
    else:
        return False


def straightFlush(h):
    return flush(h) and straight(h)


def four(h):
    s = ' '.join(list(h))
    for v in VALUES:
        if s.count(v) == 4:
            return True
    return False


def fullHouse(h):
    return pair(h)[0] and three(h)


def flush(h):
    s = ' '.join(list(h))
    return (s.count("C") == 5) or (s.count("D") == 5) or (s.count("H") == 5) or (s.count("S") == 5)


def straight(h):
    s = ' '.join(list(h))
    i = 0
    j = 0

    while i < 9:
        if s.count(VALUES[i]) == 1:
            j = i
            for _ in range(5):
                if s.count(VALUES[j]) == 1:
                    j += 1
                else:
                    break
            if j-i == 5:
                return True
            i += 1
        else:
            i += 1
    return False


def three(h):
    s = ' '.join(list(h))
    for v in VALUES:
        if s.count(v) == 3:
            return True
    return False 


def twoPair(h):
    s = ' '.join(list(h))
    newValues  = deepcopy(VALUES)
    for v in newValues:
        if s.count(v) == 2:
            newValues.remove(v)
            for v in newValues:
                if s.count(v) == 2:
                    return True
    return False


def pair(h):
    s = ' '.join(list(h))
    for v in VALUES:
        if s.count(v) == 2:
            return (True, v)
    return (False, None)


def high(hand1, hand2):
    # Check for any picture cards
    s1 = ' '.join(list(hand1))
    s2 = ' '.join(list(hand2))

    if s1.count("A") != 0:
        return 1, "A"
    elif s2.count("A") != 0:
        return 2, "A"
    elif s1.count("K") != 0:
        return 1, "K"
    elif s2.count("K") != 0:
        return 2, "K"
    elif s1.count("Q") != 0:
        return 1, "Q"
    elif s2.count("Q") != 0:
        return 2, "Q"
    elif s1.count("J") != 0:
        return 1, "J"
    elif s2.count("J") != 0:
        return 2, "J"


    # Filter the picture cards out and change the T to 10 ready for sorting
    hand1_new = []
    for card in list(hand1):
        if card.count("T") != 0:
            hand1_new.append(10)
        elif (card.count("A") + card.count("K") + card.count("Q") + card.count("J")) == 0:
            hand1_new.append(int(card[0]))


    hand2_new = []
    for card in list(hand2):
        if card.count("T") != 0:
            hand2_new.append(10)
        elif (card.count("A") + card.count("K") + card.count("Q") + card.count("J")) == 0:
            hand2_new.append(int(card[0]))


    # Sort and pick the highest as the winner
    hand1_new.sort()
    hand2_new.sort()


    if hand1_new[-1] > hand2_new[-1]:
        return 1, hand1_new[-1]
    else:
        return 2, hand2_new[-1]


def main():

    # p is a list of tuples each containing a hand for player 1 and 2
    print("opening file")
    with open("poker.txt", "r") as f:
        pOld = f.readlines()
        p = []
        for line in pOld:
            p.append((line.strip()[:14].split(), line.strip()[15:].split()))
    print("file read successfully")

    player1 = 0
    player2 = 0

    # Iterates through each tuple and determines a winner
    print("counting winners")

    f = open("results.txt", "w")

    for hand in p:
        hand1 = set(hand[0])
        hand2 = set(hand[1])

        # Check for a royal flush
        if royalFlush(hand1) == True:
            player1 += 1
            f.write(f"(1) {hand1} won by royal flush\n")
            continue
        elif royalFlush(hand2) == True:
            player2 += 1
            f.write(f"(2) {hand2} won by royal flush\n")
            continue


        # Check for straight flush
        if straightFlush(hand1) == True:
            player1 += 1
            f.write(f"(1) {hand1} won by straight flush\n")
            continue
        elif straightFlush(hand2) == True:
            player2 += 1
            f.write(f"(2) {hand2} won by straight flush\n")
            continue


        # Check for four of a kind
        if four(hand1) == True:
            player1 += 1
            f.write(f"(1) {hand1} won by four\n")
            continue
        elif four(hand2) == True:
            player2 += 1
            f.write(f"(2) {hand2} won by four\n")
            continue


        # Check for full house
        if fullHouse(hand1) == True:
            player1 += 1
            f.write(f"(1) {hand1} won by full house\n")
            continue
        elif fullHouse(hand2) == True:
            player2 += 1
            f.write(f"(2) {hand2} won by full house\n")
            continue


        # Check for flush
        if flush(hand1) == True:
            player1 += 1
            f.write(f"(1) {hand1} won by flush\n")
            continue
        elif flush(hand2) == True:
            player2 += 1
            f.write(f"(2) {hand2} won by flush\n")
            continue


        # Check for straight:
        if straight(hand1) == True:
            player1 += 1
            f.write(f"(1) {hand1} won by straight\n")
            continue
        elif straight(hand2) == True:
            player2 += 1
            f.write(f"(2) {hand2} won by straight\n")
            continue


        # Check for three of a kind
        if three(hand1) == True:
            player1 += 1
            f.write(f"(1) {hand1} won by three\n")
            continue
        elif three(hand2) == True:
            player2 += 1
            f.write(f"(2) {hand2} won by three\n")
            continue


        # Check for 2 pairs
        if twoPair(hand1) == True:
            player1 += 1
            f.write(f"(1) {hand1} won by 2 pair\n")
            continue
        elif twoPair(hand2) == True:
            player2 += 1
            f.write(f"(2) {hand2} won by 2 pair\n")
            continue


        p1 = pair(hand1)
        p2 = pair(hand2)


        # Check for pair
        if (p1[0] == True) and (p2[0] == True):
            # If the same pair, check other cards
            if p1[1] == p2[1]:
                # Remove the 2 pairs from the set
                try:
                    hand1.remove(f"{p1[1]}H")
                except:
                    pass
                try:
                    hand2.remove(f"{p2[1]}H")
                except:
                    pass
                try:
                    hand1.remove(f"{p1[1]}D")
                except:
                    pass
                try:
                    hand2.remove(f"{p2[1]}D")
                except:
                    pass
                try:
                    hand1.remove(f"{p1[1]}S")
                except:
                    pass
                try:
                    hand2.remove(f"{p2[1]}S")
                except:
                    pass
                try:
                    hand1.remove(f"{p1[1]}C")
                except:
                    pass
                try:
                    hand2.remove(f"{p2[1]}C")
                except:
                    pass

                # Run the high card function on the rest of the cards
                if high(hand1, hand2)[0] == 1:
                    player1 += 1
                    f.write(f"(1) {hand1} won by high card {high(hand1, hand2)[1]} and pair {p1[1]}\n")
                    continue
                else:
                    player2 += 1
                    f.write(f"(2) {hand2} won by high card {high(hand1, hand2)[1]} and pair {p2[1]}\n")
                    continue

            # Check whos pair is higher
            elif high(p1[1], p2[1])[0] == 1:
                player1 += 1
                f.write(f"(1) {hand1} won by a higher pair {high(hand1, hand2)[1]}\n")
                continue
            elif high(p1[1], p2[1])[0] == 2:
                player2 += 1
                f.write(f"(2) {hand2} won by a higher pair {high(hand1, hand2)[1]}\n")
                continue
        elif p1[0] == True:
            player1 += 1
            f.write(f"(1) {hand1} won by pair\n")
            continue
        elif p2[0] == True:
            player2 += 1
            f.write(f"(2) {hand2} won by pair\n")
            continue
        

        # High card wins 
        if high(hand1, hand2)[0] == 1:
            player1 += 1
            f.write(f"(1) {hand1} won by high card {high(hand1, hand2)[1]}\n")
            continue
        else:
            player2 += 1
            f.write(f"(2) {hand2} won by high card {high(hand1, hand2)[1]}\n")
            continue
        

    print(f"Player 1 has won {player1} times!")
    print(f"Player 2 has won {player2} times!")


    f.close()

if __name__ == "__main__":
    main()