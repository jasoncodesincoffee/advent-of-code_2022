def scoring_key(hand):
    if hand == 'X':
        return 1
    elif hand == 'Y':
        return 2
    elif hand == 'Z':
        return 3

def who_won(their_hand, your_hand):
    if their_hand == 'A':
        if your_hand == 'X':
            return 3
        elif your_hand == 'Y':
            return 6
        else:
            return 0
    if their_hand == 'B':
        if your_hand == 'X':
            return 0
        elif your_hand == 'Y':
            return 3
        else:
            return 6
    if their_hand == 'C':
        if your_hand == 'X':
            return 6
        elif your_hand == 'Y':
            return 0
        else:
            return 3


def stupid_rulez(opponent_hand, outcome):
    if outcome == 'X': # need to lose
        if opponent_hand == 'A':
            return 'Z'
        elif opponent_hand == 'B':
            return 'X'
        else:
            return 'Y'
    elif outcome == 'Y': # need a draw
        if opponent_hand == 'A':
            return 'X'
        elif opponent_hand == 'B':
            return 'Y'
        else:
            return 'Z'
    if outcome == 'Z': # need to win
        if opponent_hand == 'A':
            return 'Y'
        elif opponent_hand == 'B':
            return 'Z'
        else:
            return 'X'


total_score = 0
stupid_score = 0
with open('day2_input.txt', 'r') as file:
    opponent_score = []
    my_score = []
    for line in file:
        score = line.split()
        total_score += (scoring_key(score[1]) + who_won(score[0], score[1]))
        my_hand = stupid_rulez(score[0], score[1])
        stupid_score += (scoring_key(my_hand) + who_won(score[0], my_hand))

print(f'My total score is {total_score}.')
print(f'Using the stupid scoring rulez my total score is {stupid_score}.')