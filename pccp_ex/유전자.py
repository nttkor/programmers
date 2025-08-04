def get_ans(stack):
    # stack에 담긴 자손 인덱스를 거슬러 올라가며 'RR' 또는 'rr'을 찾습니다.
    while stack:
        c_idx = stack.pop()
        if c_idx == 0:  # 'RR' 유전자형
            return "RR"
        if c_idx == 3:  # 'rr' 유전자형
            return "rr"
    # 'RR'이나 'rr'이 없었다면 모두 'Rr'입니다.
    return "Rr"

def solution(queries):
    answer = []
    
    for n, p in queries:
        # 1-based 인덱스를 0-based로 변경
        n -= 1
        p -= 1
        
        stack = []
        
        while n > 0:
            # 부모 세대로 거슬러 올라가면서 현재 위치(p)를 4로 나누어 자손 위치(c)를 찾고
            # 부모 위치(p)를 갱신합니다.
            p, c = divmod(p, 4)
            stack.append(c)
            n -= 1
        
        # 스택에 저장된 자손 위치를 바탕으로 최종 유전자형을 결정합니다.
        answer.append(get_ans(stack))

    return answer

def mysolution(queries):
    answer = []
    for n, p in queries:
        stack = []
        p -= 1
        for i in range(n-1):
            m = p % 4 
            p //= 4
            stack.append((p,m))
        current = [0,1,1,3]
        parent={0:[0,0,0,0],1:[0,1,1,3],2:[0,1,1,3],3:[3,3,3,3]}
        symbol = {0:'RR',1:'Rr',2:'Rr',3:'rr'}
        while(stack):
            n,p = stack.pop()
            current = parent[current[p]]
        answer.append(symbol[p])
    return answer