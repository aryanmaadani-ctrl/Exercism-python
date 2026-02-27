def is_criticality_balanced(temperature ,number_of_neutrons):
    if temperature  < 800.00 and number_of_neutrons > 500.00 and number_of_neutrons * temperature < 500000:
        return True
    else:
        return False

def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power)* 100
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60 and  efficiency < 80:
        return 'orange'
    elif efficiency >= 30 and efficiency < 60:
        return 'red'
    else:
        return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    x = temperature * neutrons_produced_per_second
    ten_percent_of_threshold = (threshold * 10) / 100
    if x <= ((threshold * 90) / 100):
        return 'LOW'
    elif x < (threshold + ten_percent_of_threshold) and x > (threshold - ten_percent_of_threshold):
        return 'NORMAL'
    else:
        return 'DANGER'

print(fail_safe(10, 1101, 10000))
