
a = [
'3 1 1',
'1 6 7',
'2 5 8',
'3 4 9']

b= ['4 2 2',
'1 2 2 3',
'3 5 10 15',
'3 8 11 2',
'4 5 4 4']
c=a
def myinput(L):
    for string in L:
        yield string
gen = myinput(b)
n, r, c = map(int, next(gen).split())
a = [[0] * (n + 1) for _ in range(n + 1)]


for i in range(1, n + 1):
    row = list(map(int, next(gen).split()))
    for j in range(1, n + 1):
        a[i][j] = row[j - 1]

def isInside(x,y):
    '''
    check boundery of grid
    '''
    return 0< x <= n and 0< y <= n
# Please write your code here.

movable = True
dirs = [(0,1),(0,-1),(-1,0),(1,0)]
cx,cy = c,r
path = [a[cy][cx]]
while True:
    movable = False
    for dx,dy in dirs:
        nx, ny = cx+dx, cy+dy
        if isInside(nx,ny) and a[cy][cx] < a[ny][nx]:
            path.append(a[ny][nx])
            cx,cy = nx, ny
            movable = True
            break
    if movable == False:
        break

for n in path:
    print(n,end=' ')
    
