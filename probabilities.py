import itertools
from collections import defaultdict
import operator
from random import randint

from evaluate import *


def variations(dices):
    return [(dices[0] + dices[1],
             dices[2] + dices[3]),
            (dices[0] + dices[2],
             dices[1] + dices[3]),
            (dices[0] + dices[3],
             dices[1] + dices[2])]


DICE_COMBINATIONS = list(map(variations, itertools.product(
    * [range(1, 7), range(1, 7), range(1, 7), range(1, 7)])))


def coef(n):
    return (14/(7 - abs(n - 7)))


def detect_combinations(rowed_deices):
    S = 0
    for i in DICE_COMBINATIONS:
        for (dice1, dice2) in rowed_deices:
            if (dice1, dice2) in i or (dice2, dice1) in i:
                S += 1
                break

    return S/len(DICE_COMBINATIONS)


def P_before(rope1=None, rope2=None, rope3=None, taken_ropes=set()):
    existing_ropes = [i for i in [rope1, rope2, rope3] if i != None]
    S = 0
    for possible_throws in DICE_COMBINATIONS:
        for rope in existing_ropes:
            for throw in possible_throws:
                if rope in throw:
                    S += 1
                    break

    return S/len(DICE_COMBINATIONS)


def P_after(rope1=None, rope2=None, rope3=None, taken_ropes=set()):
    S = 0
    for possible_throws in DICE_COMBINATIONS:
        for i in possible_throws:
            if (rope1 in i or rope2 in i or rope3 in i) \
                    and ({i[0], i[1]} - taken_ropes != set()):
                S += 1
                break

    return S/len(DICE_COMBINATIONS)


def P(rope1=None, rope2=None, rope3=None, taken_ropes=set()):
    if rope1 and rope2 and rope3:
        P_after(rope1, rope2, rope3, taken_ropes)
    else:
        P_before(rope1, rope2, rope3, taken_ropes)


def notP(rope1=None, rope2=None, rope3=None):
    pass    
    

def generate_dices():
    return randint(1, 6), randint(1, 6), randint(1, 6), randint(1, 6)


if __name__ == "__main__":
    pass
