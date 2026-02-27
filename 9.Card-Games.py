def get_rounds(round_number):
    round_number2 = round_number + 1
    round_number3 = round_number2 + 1
    return [round_number, round_number2, round_number3]


def concatenate_rounds(rounds_1, rounds_2):
    return rounds_1 + rounds_2


def list_contains_round(rounds, round_number):
    if round_number in rounds:
        return True
    else:
        return False


def card_average(hand):
    return sum(hand) / len(hand)


def approx_average_is_average(hand):
    average_of_first_and_last = (hand[0]+hand[-1]) / 2
    median = hand[int((len(hand) / 2))]
    actual_average = card_average(hand)
    if average_of_first_and_last == actual_average or median == actual_average:
        return True
    else:
        return False



def average_even_is_average_odd(hand):
    odd_average =  sum(hand[::2]) / len(hand[::2])
    even_average = sum(hand[1::2]) / len(hand[1::2])
    if odd_average == even_average:
        return True
    else:
        return False

def maybe_double_last(hand):
    jack = hand[-1] * 2
    new_list = hand[:-1] + [jack]
    if hand[-1] == 11:
        return new_list
    else:
        return hand
