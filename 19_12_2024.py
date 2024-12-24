#14215 세 막대
#삼각형 성립조건 식 까먹어서 못 풀음 a<b<c 일때 a+b>c이여야하고 이게 성립하지 않을 경우엔
#c를 a+b-1로 바꿔 최대 둘레 삼각형을 만들 수 있다
a, b, c = sorted(map(int, input().split()))

if a + b > c:
    print(a + b + c)
else:
    print(2 * (a + b) - 1)
    
#24262 시간복잡도
#상당히 이상한 문제인데 그냥 주어진 함수의 시간복잡도를 생각해보는 문제인 것 같네
print(1)  # f(n)의 최고차항 계수 a
print(0)  # 시간 복잡도의 차수 O(1)에서 차수는 0

#24263 알고리즘 수업 - 알고리즘의 수행 시간 2
#이것도 마찬가지로 음 그냥 분석 문제, 의사 코드가 익숙하지 않아서 쉬프트 미는 연산인줄 알았다.
#for문이 하나이므로 최고차항 1
a = int(input())

print(a)
print(1)

#24264 알고리즘 수행시간 3
#같은 맥락이다, 포문이 2 중첩이니 차수는 n^2가 되겠지
a = int(input())

print(a**2)
print(2)

# 반복 횟수 공식:
# 범위에 있는 값의 개수는 다음과 같이 계산됩니다:
# 반복 횟수=(끝값−시작값)+1

#24265 알고리즘 수행시간 4
#시그마 계산이 익숙하지가 않아서 좀 헤맸다
# 입력 받기
n = int(input())

# 결과 출력
print(n * (n - 1) // 2)  # 수행 횟수
print(2)                # 최고차항 차수

#24266 수행시간 5
#간단하게 나와서 다행이네 그냥 n 3승
n = int(input())

print(n**3) 
print(3)

#24267 수행시간 6
#시그마 계산이 어렵다
# 입력 받기
n = int(input())

# 수행 횟수 계산
execution_count = n * (n - 1) * (n - 2) // 6

# 결과 출력
print(execution_count)
print(3)

#24313 다시보자

#2798 블랙잭 - 브루트 포스로 풀기 혹은 그냥 조합 라이브러리

#브루트포스 버젼
# 입력 처리
N, M = map(int, input().split())  # N: 카드 개수, M: 합의 최대값
arr = list(map(int, input().split()))  # 카드에 적힌 숫자 리스트

# 결과 초기화
result = 0

# 카드 3장을 고르는 모든 조합을 탐색
for i in range(N):  # 첫 번째 카드
    for j in range(i+1, N):  # 두 번째 카드 (i 이후부터 선택)
        for k in range(j+1, N):  # 세 번째 카드 (j 이후부터 선택)
            # 카드 3장의 합 계산
            total = arr[i] + arr[j] + arr[k]
            # 합이 M 이하이면서 최대값 갱신
            if total <= M:
                result = max(result, total)

# 결과 출력
print(result)

#2231 분해합
#식을 세우는게 아주 쉽지가 않았다.
#하지만 분해합 식을 보면 분해합S= 생성자 + 생성자 각 자리수의 합이라는 것을 알 수 있다.
#이걸로 생성자 = 분해합 - 각 자리수의 합이므로 식을 세울 수 있다.

# 입력
N = int(input())

# 최소 생성자를 찾기 위한 초기값 설정
min_creator = 0

# 가능한 범위 탐색 (N - 자리 수 * 9)
start = max(1, N - len(str(N)) * 9)  # 생성자가 존재할 최소 범위
for i in range(start, N):
    # 분해합 계산
    digit_sum = sum(map(int, str(i)))  # 각 자리 숫자의 합
    if i + digit_sum == N:
        min_creator = i
        break

# 결과 출력
print(min_creator)

#19532 브루트포스 풀이
a, b, c, d, e, f = map(int, input().split())

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (a*i) + (b*j) == c and (d*i) + (e*j) == f:
            print(i,j)
#혹은 연립방정식 그냥 풀기
a, b, c, d, e, f = map(int, input().split())

print((c*e-b*f)//(a*e-b*d), (a*f-d*c)//(a*e-b*d))

# 크래머의 법칙(Cramer's Rule)은 선형 방정식 시스템을 행렬을 사용하여 푸는 방법 중 하나입니다. 주어진 연립방정식을 행렬 형태로 표현하고, 행렬식(Determinant)을 이용하여 해를 구하는 방법입니다.
# 예를 들어, 다음과 같은 두 개의 연립방정식이 있다고 가정합니다:
# ax + by = c
# dx + ey = f
# 이를 행렬 형태로 표현하면 다음과 같습니다:
# | a  b | | x | = | c |
# | d  e | | y |   | f |
# 크래머의 법칙에 따르면, 이 연립방정식의 해 (x, y)는 다음과 같이 구할 수 있습니다:
# x = (ce - bf) / (ae - bd)
# y = (af - cd) / (ae - bd)

#1018 체스판 다시 칠하기
#생각보다 어려웠다, 블로그 참고함
a, b = map(int, input().split())
board = [input() for _ in range(a)]

def count_repaints(board, start_row, start_col, first_color):
    repaints = 0
    for i in range(8):
        for j in range(8):
            expected_color = first_color if (i + j) % 2 == 0 else ('B' if first_color == 'W' else 'W')
            if board[start_row + i][start_col + j] != expected_color:
                repaints += 1
    return repaints

min_repaints = float('inf')

#체스판 시작점 정하기
for i in range(a - 7):
    for j in range(b - 7):
        repaints_w = count_repaints(board, i, j, 'W')
        repaints_b = count_repaints(board, i, j, 'B')
        min_repaints = min(min_repaints, repaints_w, repaints_b)

print(min_repaints)