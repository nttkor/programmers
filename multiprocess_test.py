def generator(pattern, n):
    def dfs(combi, cnt):
        if cnt == n:
            yield combi
            return  # 여기서 종료해줘야 아래 루프 안 탐
        for v in pattern:
            if v in combi:   # 중복 없이
                continue
            # 재귀 제너레이터의 값을 바깥으로 내보내기
            yield from dfs(combi + v, cnt + 1)

    # dfs가 만들어낸 제너레이터를 반환해야 함
    return dfs('', 0)

# 사용 예시
gen = generator("1234", 4)
for v in gen:
    print(v)