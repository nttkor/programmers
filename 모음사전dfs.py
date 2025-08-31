def solution(word):
    dic = "AEIOU"
    idx = [0, 0]  # [현재 인덱스, 정답 위치]

    def dfs(cnt, s):
        if cnt <= 5:
            idx[0] += 1
            if s == word:
                idx[1] = idx[0]
                return True   # 찾았음을 알림
        else:
            return False

        for i in range(5):
            if dfs(cnt+1, s+dic[i]):  # 하위 호출이 True면 바로 종료
                return True
        return False

    dfs(0, '')
    return idx[1]

word = "AAAAE"
print(solution(word))  # → 6
