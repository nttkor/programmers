a = [[ i*10+j for j in range(1,3)] for i in range(1,4)]
b = [[ i*10+j for j in range(1,5)] for i in range(1,3)]
ar, bc = len(a), len(b[0])
ab = [[ i*10+j for j in range(1,bc+1)] for i in range(1,ar + 1)]
print('a', *a, 'b', *b,'ab',*ab, sep='\n')

def dot(a,b):
    return sum([i*100+j for i,j in zip(a,b)])

bt = list(zip(*b))
ab = [[ dot(i,j) for j in bt] for i in a]
print(ab)