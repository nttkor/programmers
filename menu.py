
def solution(menu, order, k):
    answer = 0
    cnt = 0
    ctime = 0
    wtime = 0
    wait = 0
    pt = 0
    while order:
        if pt > 0:
            pt = pt - k
            if pt >= 0:
                wait += 1
                ctime += min(pt,k)
            else:
                pt = 0
            print(ctime, m,pt, wait)
        else:
            if wait >0:
                wait -= 1
            m = order.pop(0)
            pt = menu[m]
            print(ctime, m,pt, wait)
            ctime += k



    return answer
menu = [5, 12, 30]
order = [1, 2, 0, 1]
k = 10
solution(menu,order,k)