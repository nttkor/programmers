from itertools import permutations
def solution(ability):
    answer = 0
    y = len(ability)
    x = len(ability[0])

    perm = permutations(range(y),x)
    max = 0
    for p in perm:
        sum = 0
        for i,v in enumerate(p):
            sum += ability[v][i]
        if sum > max :
            max = sum
    answer = max
    return answer