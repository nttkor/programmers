def dot(a, b):
    return sum(i * j for i, j in zip(a, b))
    
a = [[j for j in range(1, 3)] for i in range(1, 4)]
b = [[i for j in range(1, 5)] for i in range(1, 3)]

print('a', *a, 'b', *b, sep='\n')

bt = list(zip(*b))
ab = [[dot(i, j) for j in bt] for i in a]
print('ab', *ab, sep='\n')