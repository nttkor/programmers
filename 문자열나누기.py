def solution(s):
    answer = 0
    prev = ''
    cnt1, cnt2 = 0, 0
    for ch in s:
        if cnt1 == 0:
            prev = ch
            cnt1 += 1
            continue
        if ch == prev:
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            answer += 1
            cnt1 == 0
            cnt2 == 0
            prev = ch
    if cnt1 > 0:
        answer += 1
    return answer

s = "abracadabra"
solution(s)