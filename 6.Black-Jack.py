def value_of_card(card):
    if card in ["2","3","4","5","6","7","8","9"]:
        return int(card)
    elif card == "A":
        return 1
    elif card in ["K", "Q", "J", "10"]:
        return 10
    else:
        return 0

def higher_card(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    if v1 > v2:
        return card_one
    elif v1 < v2:
        return card_two
    elif v1 == v2:
        return card_one, card_two
    else:
        return "invalid card"

def value_of_ace(card_one, card_two):

    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if card_one == "A" or card_two == "A":
        return 1

    if v1 + v2 + 11 > 21:
        return 1
    else:
        return 11

def is_blackjack(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)

    if (card_one == "A" and v2 == 10) or (card_two == "A" and v1 == 10):
        return True
    else:
        return False


def can_split_pairs(card_one, card_two):
    v1 = value_of_card(card_one)
    v2 = value_of_card(card_two)
    if v1 == v2:
        return True
    else:
        return False

def can_double_down(card_one, card_two):
    total = value_of_card(card_one) + value_of_card(card_two)
    if total in [9, 10, 11]:
        return True  
    else:
        return False
