
def solution(word):
    answer = 0
    dic = []
    from itertools import product
    for i in range(5):
        products = product('AEIOU',repeat=i+1)
        for p in products:
            dic.append(''.join(p))
    dic.sort()
    idx = dic.index(word)
    return idx+1
word = "I"
idx = solution(word)
print(idx)