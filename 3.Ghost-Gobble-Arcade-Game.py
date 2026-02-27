def eat_ghost(power_pellet_active, touching_ghost):
    able_to_eat = power_pellet_active and touching_ghost
    return able_to_eat

print(eat_ghost(True, True))


def score(touching_power_pellet, touching_dot):
    x = touching_power_pellet or touching_dot
    return x

print(score(True, False))


def lose(power_pellet_active, touching_ghost):
    power_pellet_deactive = not power_pellet_active
    packman_lose = touching_ghost and  power_pellet_deactive
    return packman_lose
print(lose(False, True))


def win(eaten_all_dots,power_pellet_active,touching_ghost):
    packman_lose = lose(power_pellet_active, touching_ghost)
    packman_wins = eaten_all_dots and not packman_lose
    return packman_wins

print(win(True,False,False))
