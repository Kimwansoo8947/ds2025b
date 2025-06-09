import math
import sys

def is_prime(n) -> bool:
    if n<=1: # 1 이하는 소수가 아니다.
        return False
    elif n == 2: # 2는 소수
        return True
    elif n %2 == 0: # 짝수는 2를 제외하고 소수가 아니다.
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1,2): # 홀수만 검사
            if n % i ==0: # 나누어 떨어지면 소수가 아니다.
                return False
        return True # 위 조건을 모두 만족하면 소수


s,e = map(int, input().split())
for i in range(s, e+1):
    if is_prime(i):
        print(i)