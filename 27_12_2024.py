#13241 최소공배수
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# 입력 받기
a, b = map(int, input().split())

# 최소공배수 계산
result = lcm(a, b)

# 결과 출력
print(result)

#1735 분수 합
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 입력 받기
a1, b1 = map(int, input().split())
a2, b2 = map(int, input().split())

# 분수 합 계산
numerator = a1 * b2 + a2 * b1  # 분자
denominator = b1 * b2          # 분모

# 최대공약수로 약분
g = gcd(numerator, denominator)
numerator //= g
denominator //= g

# 결과 출력
print(numerator, denominator)

#2485 가로수
import sys
import math
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 입력 받기
N = int(input().strip())
positions = [int(input().strip()) for _ in range(N)]

# 가로수 사이의 간격 계산
distances = [positions[i] - positions[i - 1] for i in range(1, N)]

# 모든 간격의 최대공약수 구하기
g = distances[0]
for d in distances[1:]:
    g = gcd(g, d)

# 추가해야 하는 가로수의 개수 계산
total_trees = (positions[-1] - positions[0]) // g + 1
additional_trees = total_trees - N

# 결과 출력
print(additional_trees)

#4134 다음 소수
import sys
input=sys.stdin.readline
N=int(input())

def check(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return False
    return True

for i in range(N):
    n=int(input())
    while True:
        if n==0 or n==1:
            print(2)
            break
        if check(n):
            print(n)
            break
        else:
            n+=1

# 소수 판별 원리:
# 소수의 정의:

# 소수는 1과 자기 자신 외에는 약수가 없는 1보다 큰 자연수입니다.
# 제곱근까지만 검사하는 이유:

# 어떤 수 n이 소수가 아니라면, n은 두 개의 자연수 a와 b의 곱으로 표현될 수 있습니다 (n = a * b).
# 이때, a와 b 중 적어도 하나는 n의 제곱근 이하입니다. 그렇지 않으면 두 수의 곱이 n보다 커지기 때문입니다.
# 예를 들어, n = 36인 경우:
# 약수 쌍은 (1, 36), (2, 18), (3, 12), (4, 9), (6, 6)입니다.
# 여기서 6은 36의 제곱근입니다.
# 제곱근보다 큰 약수는 제곱근 이하의 약수와 짝을 이루기 때문에, 제곱근까지만 검사하면 충분합니다.

#4948 베르트랑 공준
import sys
input = sys.stdin.readline

def sieve_of_eratosthenes(max_num):
    is_prime = [True] * (max_num + 1)
    is_prime[0] = is_prime[1] = False
    p = 2
    while p * p <= max_num:
        if is_prime[p]:
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    return is_prime

# 에라토스테네스의 체를 사용하여 2 * 123456까지의 소수를 미리 구해둠
max_num = 2 * 123456
is_prime = sieve_of_eratosthenes(max_num)

# 입력 받기 및 결과 출력
while True:
    n = int(input().strip())
    if n == 0:
        break
    count = sum(is_prime[n + 1:2 * n + 1])
    print(count)
    
#13909 창문 닫기
import sys
import math
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())

# 1부터 N까지의 완전 제곱수의 개수 계산
result = int(math.sqrt(N))

# 결과 출력
print(result)