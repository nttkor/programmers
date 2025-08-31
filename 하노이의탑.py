def solution(n):
    def hanoi(n, fr, to, tem):
        if n == 1:
            print(f'{fr} to {to}')
            return
        hanoi(n-1,fr, tem, to)
        print(f'{fr} to {to}')
        hanoi(n-1, tem,to,fr)
    hanoi(n,1,3,2)
solution(2)

