def solution(s):
    answer = [0,0]
    def bconv(string):
        b = ''
        cnt = 0
        for v in string:
            if v == '1':
                b += v
            else:
                cnt += 1
        return format(len(b),'b'), cnt

    i=0
    st = s
    while st != '1':
        st, cnt = bconv(st)
        slen = len(st)
        answer[0] +=1 
        answer[1] += cnt
        i += 1
    return answer

s = "110010101001"
x = solution(s)
print(x)