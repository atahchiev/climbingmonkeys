import itertools

from collections import defaultdict

def ways(dice):
    if dice <= 7 and dice >= 1:
        return dice - 1
    elif dice > 7 and dice <= 12:
        return 6 - (dice % 7)
    else:
        return dice

def combinations_fornumber(dice):
    if dice <= 7 and dice >= 1:
        return [(dice - i, i) for i in range(1, dice) ]
    elif dice >= 7 and dice <= 13:
        return [(dice - i, i) for i in range(dice - 6, 7) ]
print(combinations_fornumber(9))


def is_it_possible(l, combination):
    for i in l:
        if set(i).issubset(combination):
            return True
    return False

def variations(combinaitons):
    return {combinaitons[0] + combinaitons[1],
            combinaitons[2] + combinaitons[3],
        combinaitons[0] + combinaitons[2],
            combinaitons[1] + combinaitons[3],
        combinaitons[0] + combinaitons[3],
            combinaitons[1] + combinaitons[2]}


all_sums = list(map(variations, itertools.product(* [range(1,7), range(1,7), range(1,7), range(1,7)])))
diffrent = list(filter(lambda x: len(set(x)) == 3, itertools.product(* [range(2,13), range(2,13), range(2,13)])))

# print(diffrent)

def P(a=None, b=None, c=None):
    S = 0
    if a and b and c:
        for i in all_sums:
            if a in i or b in i or c in i:
                S += 1
            return S

    if a and not b and not c:
        for i in all_sums:
            if a in i or b in i or c in i:
                S += 1
            return S

    if a and not b and not c:
        for i in all_sums:
            if a in i or b in i or c in i:
                S += 1
            return S
def notP(a=None, b=None, c=None):
    pass
print(len(diffrent))
print(P(6,7,8))



def init_takova():
    # print(all_combinaions)

    combinations = defaultdict(list)
    for i in range(2, 13):
        S = 0
        for j in all_sums:
            if i in j:
                S += 1

        combinations[i] =S
        S = 0
    return combinations

print(init_takova())

itertools.product(* [range(1,7), range(1,7)])
# print ([{i: [ (i, j) for j in range(1, i + 1) if j == 1 ]} for i in range(1, 13)])

