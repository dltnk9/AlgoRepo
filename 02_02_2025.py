#24723 녹색거탑
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())

# 녹색거탑을 쌓는 방법의 수 계산
result = 2 ** N

# 결과 출력
print(result)

#10872 팩토리얼
import sys
input = sys.stdin.readline

def factorial(n):
    if n ==0 or n==1:
        return 1
    return n*factorial(n-1)

N = int(input().strip())

result = factorial(N)

print(result)

#11050 이항 계수 1
import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 입력 받기
N, K = map(int, input().strip().split())

# 이항 계수 계산
result = factorial(N) // (factorial(K) * factorial(N - K))

# 결과 출력
print(result)

#1010 다리 놓기
import sys
input = sys.stdin.readline

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 입력 받기
T = int(input().strip())
results = []

for _ in range(T):
    N, M = map(int, input().strip().split())
    # 이항 계수 계산
    result = factorial(M) // (factorial(N) * factorial(M - N))
    results.append(result)

# 결과 출력
for result in results:
    print(result)