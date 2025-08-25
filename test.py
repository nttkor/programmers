word = 'abcAbCde'
answer = ''
for i,v in enumerate(word):
    if v.isupper():
        answer += v.lower()
    else:
        answer +=  v.upper()
print(word)