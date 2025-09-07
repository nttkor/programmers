# 더 효율적인 최대공약수 알고리즘: 유클리드 호제법
# 최대공약수를 구할 때는 **유클리드 호제법(Euclidean Algorithm)**을 사용하는 것이 훨씬 효율적이고 일반적인 방법입니다. 
# 유클리드 호제법은 두 수의 최대공약수를 구하는 가장 오래된 알고리즘으로, 반복문이나 재귀를 통해 간단하게 구현할 수 있습니다.

# 1. 반복문을 이용한 유클리드 호제법
def gcd(a, b):
    # a와 b의 최대공약수를 구하는 함수
    while b > 0:
        a, b = b, a % b
    return a

n, m = 12, 18
print(f"{n}과 {m}의 최대공약수: {gcd(n, m)}")
# 동작 원리: 두 수 a와 b가 있을 때, a를 b로 나눈 나머지를 r이라고 하면, a와 b의 최대공약수는 b와 r의 최대공약수와 같습니다. 
# b가 0이 될 때까지 이 과정을 반복하면, 마지막에 남는 a 값이 최대공약수입니다.

# 2. 재귀를 이용한 유클리드 호제법

def gcd_recursive(a, b):
    # 재귀를 이용해 최대공약수를 구하는 함수
    if b == 0:
        return a
    else:
        return gcd_recursive(b, a % b)

n, m = 12, 18
print(f"{n}과 {m}의 최대공약수: {gcd_recursive(n, m)}")


# 최소공배수 구하기
# 최소공배수(LCM: Least Common Multiple)는 최대공약수를 이용하면 더 쉽게 구할 수 있습니다. 두 수의 곱은 최대공약수와 최소공배수의 곱과 같습니다.

# 최소공배수 = (두 수의 곱) / (최대공약수)
def lcm(a, b):
    # 최소공배수 공식: (a * b) / gcd(a, b)
    # 0으로 나누는 것을 방지하기 위해 예외처리
    if a == 0 or b == 0:
        return 0
    return abs(a * b) // gcd(a, b)

n, m = 12, 18
print(f"{n}과 {m}의 최소공배수: {lcm(n, m)}")