def solution(input_string):
    answer = ''
    chk = dict()
    prev = ''
    for ch in input_string:
        if prev == ch:
            n,d = chk[ch]
            chk[ch] = n+1,d
        else:
            if ch in chk:
                n,d = chk[ch]
                chk[ch] = n+1,d+1
            else:
                chk[ch] = 1, 1
        prev = ch
        two = []
        for k, (n, d) in chk.items():
            if n >=2 and d >= 2:
                two.append(k)
        two.sort()
        answer = ''.join(two)
        if answer == '':
            answer = 'N'
    return answer