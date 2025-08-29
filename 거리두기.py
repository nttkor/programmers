places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], 
 ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], 
 ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], 
 ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], 
 ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]
 ]
def solution(places):
    answer = []
    mx = 5
    my = 5
    dir = [(1,0),(-1,0),(0,1),(0,-1)]
    being = [ (x,line) for line in places for x in line if places[line][x] == 'P' ]
    print(being)
        
    return answer

for line in places:
    print(line)
# solution(places)
