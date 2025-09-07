n=100
d=2
while d<n:
    if n%d == 0:
        print(d)
        n //= d
    else:
        d+=1
if n>1:
    print(n)