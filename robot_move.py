def solution(command):
    forward = 0
    cpos = (0,0)
    direction = {0:(0,1),1:(1,0),2:(0,-1),3:(-1,0)}
    for v in command:
        if v =='R':
            forward = (forward+1)%4
        elif v == 'L':
            forward = (forward-1+4)%4
        elif v == 'G':
            cpos = (cpos[0]+direction[forward][0], cpos[1]+direction[forward][1])
        elif v == 'B':
            forward = (forward + 2) % 4
            cpos = (cpos[0]+direction[forward][0], cpos[1]+direction[forward][1])
        print(v,forward, cpos)


    answer = list(cpos)
def solution_good(command):
    x, y = 0, 0
    forward = 0
    dirs = [(0,1), (1,0), (0,-1), (-1,0)]  # 북, 동, 남, 서

    for v in command:
        dx, dy = dirs[forward]
        if v == 'R':
            forward = (forward + 1) % 4
        elif v == 'L':
            forward = (forward - 1) % 4
        elif v == 'G':
            x += dx
            y += dy
        elif v == 'B':
            x -= dx
            y -= dy

    return [x, y]

solution("GRGLGRG")