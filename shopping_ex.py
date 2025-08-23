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
    best = 0
    nbit = (1 << n)  -1
    print('nbit',nbit)
    bit_shops = [sum((1 << i) for i, v in enumerate(shop) if v > 0) for shop in shops]
    print('bit_shop', bit_shops)
    for i in range(1, len(shops)+1):
        for combi in combinations(bit_shops,i):
            combine = 0
            for p in combi:
                print(p,end=',')
                combine |= p
            if combine == nbit:
                print('combine',combine)
                answer = (i,combi)
                return answer
                
    return answer -1, []

# 결과 출력
min_cnt , best_combination = solutions(n,shops)
print("최소 가게 수:", min_cnt)
print("방문할 가게 인덱스:", best_combination)