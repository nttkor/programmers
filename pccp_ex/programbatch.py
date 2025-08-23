def solution(program):
    answer = [ 0 for _ in range(11)]
    program.sort(key=lambda x : (x[1],x[0]))
    num = len(program)
    cnt = 0
    while cnt < num:
        score0, start0, end0 = program[cnt]
        #print(score0, start0, end0)
        answer[0] += end0
        stack = []
        for j in range(cnt+1, num):
            score1, start1, end1 = program[j]
            if  start0 <= start1 <= start0+end0:
                answer[program[j][0] ] += start0+end0 - program[j][1] 
                program[j][1] = start0+end0
                stack.append(program[j])
            else:
                break
        if stack:
            stack.sort(key=lambda x : (x[1],x[0]))

        #print('stack',stack)
        program = program[:cnt+1] + stack + program[cnt+len(stack)+1:] 
        cnt += 1
    return answer
programs = [[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]
print(solution(programs))