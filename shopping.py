from itertools import combinations
shops = [
    [0,1,1,0,0],
    [1,0,0,1,1],
    [0,1,1,1,0],
    [0,1,0,1,0],
    [1,1,0,0,0],
    [0,0,1,1,1]
]

n = 5  # 필요한 물건의 수
def solutions(n,shops):
    # 우리가 필요한 물건의 비트마스크 (모든 물건을 포함하고 있는 상태)
    # 예: n = 5이면, 이진수로 11111 => 31
    want = (1 << n) - 1  # 즉, 2^n - 1

    # 각 가게의 물건을 비트마스크로 변환
    # 예: [0,1,1,0,0] -> 01100 (12)
    # bit_shops = []
    # for shop in shops:
    #     bit = 0
    #     for i, has_item in enumerate(shop):
    #         if has_item:
    #             bit |= (1 << i)
    #     bit_shops.append(bit)

    bit_shops = [sum((1 << i) for i, has_item in enumerate(shop) if has_item) for shop in shops]

    min_cnt = float('inf')  # 최소 가게 수
    best_combination = []   # 최소 가게 조합

    # 모든 가게 조합을 순회 (1개부터 전체 가게까지)
    for r in range(1, len(bit_shops) + 1):
        for comb in combinations(enumerate(bit_shops), r):
            indices, bits = zip(*comb)
            total = 0
            for b in bits:
                total |= b  # 비트 OR로 아이템 합치기

            if total == want:  # 모든 아이템을 갖춘 조합이라면
                if r < min_cnt:
                    min_cnt = r
                    best_combination = list(indices)
    return min_cnt, best_combination

# 결과 출력
min_cnt , best_combination = solutions(n,shops)
print("최소 가게 수:", min_cnt)
print("방문할 가게 인덱스:", best_combination)