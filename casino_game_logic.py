import random


def spin_roulette():
    return random.randint(0, 30)


def play_round(capital, bet):
    result = spin_roulette()
    if result == bet:
        return capital + bet, True
    else:
        return capital - 100, False
