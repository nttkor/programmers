from itertools import combinations
shops = [
    [0,1,1,0,0],
    [0,0,0,1,1],
    [0,1,0,1,0],
    [0,1,0,1,0],
    [1,1,0,0,0],
    [0,0,1,0,1]
]
n = 5
def solutions(n,shops):
    answer = 0
    want = set(range(n))
    shop_sets = [{i for i,v in enumerate(shop) if v } for shop in shops]
    for r in range(1,len(shops)+1):
        for combi in combinations(range(len(shops)),r):
            u = set()
            for i in combi:
                u = u | shop_sets[i]
            if u == want:
                answer = r
                return answer


    return -1
n= solutions(n,shops)
print("최소 가게 수:", n)