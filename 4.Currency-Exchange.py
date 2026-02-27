def exchange_money(budget, exchange_rate):
    return budget / exchange_rate

print(exchange_money(127.5, 1.2))

def get_change(budget, exchanging_value):
    return budget - exchanging_value
print(get_change(127.5, 120))

def get_value_of_bills(denomination, number_of_bills):
    # if number_of_bills / denomination:
        return denomination * number_of_bills
print(int(get_value_of_bills(5, 128)))

def get_number_of_bills(amount, denomination):
    return int((amount / denomination))
print(get_number_of_bills(127.5, 5))

def get_leftover_of_bills(amount, denomination):
    return amount % denomination
print(get_leftover_of_bills(127.5, 20))

def exchangeable_value(budget,exchange_rate, spread, denomination):
    new_exchange_rate = exchange_rate * ((spread / 100) + 1)
    value_after_exchange = budget / new_exchange_rate
    return (value_after_exchange // denomination) * denomination
print(exchangeable_value(100000, 10.61, 10, 1))
