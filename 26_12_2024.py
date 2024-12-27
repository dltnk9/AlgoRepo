#14425 문자열 집합
import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())

# 문자열 집합 S를 저장할 집합
S = set()

# N개의 문자열을 집합 S에 추가
for _ in range(N):
    S.add(input().strip())

# M개의 문자열을 확인하고, 집합 S에 포함되어 있는지 확인
count = 0
for _ in range(M):
    if input().strip() in S:
        count += 1

# 결과 출력
print(count)

#7785 회사에 있는 사람람
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input())

# 문자열 집합 S를 저장할 집합
S = dict()

for _ in range(N):
    a,b = input().split()
    if(b == 'enter'):
        S[a] = b
    elif(b == 'leave'):
        del S[a]

for key in sorted(S.keys(), reverse=True):
    print(key)
    
#1620 나는야 포켓몬 마스터 이다솜
#개행문자때문에 고생함. strip()을 사용하자.
#시간초과가 나옴
import sys
input = sys.stdin.readline

# 입력 받기
N,M = map(int,input().strip().split())

# 문자열 집합 S를 저장할 집합
S = dict()

for i in range(1,N+1):
    a = input().strip()
    S[i] = a

# print(S)
for j in range(M):
    b = input().strip()
    if b.isalpha():
        indices = [key for key, value in S.items() if value == b] #이 부분이 시간을 다 잡아먹음
        print(indices[0])
    if b.isdigit():
        print(S[int(b)])

#결국 그냥 두 개 만들어버림
import sys
input = sys.stdin.readline

# 입력 받기
N,M = map(int,input().strip().split())

# 문자열 집합 S를 저장할 집합
S = dict()

for i in range(1,N+1):
    a = input().strip()
    S[i] = a

reverse_S = {value.strip(): key for key, value in S.items()}
for j in range(M):
    b = input().strip()
    if b.isalpha(): #문자열에 문자만 있는지 확인
        print(reverse_S.get(b))
    if b.isdigit(): #문자열에 숫자만 있는지 확인
        print(S[int(b)])

#10816 숫자 카드 2
import sys
input = sys.stdin.readline

N = int(input().strip())
list_N = list(map(int, input().split()))

M = int(input().strip())
list_M = list(map(int, input().split()))

# 숫자 카드의 개수를 저장할 딕셔너리
count_dict = {}

# 숫자 카드의 개수를 세어 딕셔너리에 저장
for num in list_N:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# 결과 저장
results = []
for m in list_M:
    if m in count_dict:
        results.append(count_dict[m])
    else:
        results.append(0)

# 결과 출력
print(' '.join(map(str, results)))

#1764 듣보잡
import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())

# 듣도 못한 사람의 집합
not_heard = set()
for _ in range(N):
    not_heard.add(input().strip())

# 보도 못한 사람의 집합
not_seen = set()
for _ in range(M):
    not_seen.add(input().strip())

# 듣도 보도 못한 사람의 집합 (교집합)
not_heard_and_seen = sorted(not_heard & not_seen)

# 결과 출력
print(len(not_heard_and_seen))
for name in not_heard_and_seen:
    print(name)

#1269 대칭 차집합
import sys
input = sys.stdin.readline

# 입력 받기
N, M = map(int, input().split())

# 집합 A와 B를 저장할 집합
A = set(map(int, input().split()))
B = set(map(int, input().split()))

# 대칭 차집합 구하기
symmetric_difference = A ^ B

# 결과 출력
print(len(symmetric_difference))


#1934 최소공배수
#유클리드 호제법으로 최대공약수 먼저 구하고 공배수 구함
import sys
input = sys.stdin.readline

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

# 입력 받기
T = int(input().strip())
results = []

for _ in range(T):
    a, b = map(int, input().split())
    results.append(lcm(a, b))

# 결과 출력
for result in results:
    print(result)

