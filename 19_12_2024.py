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

#2798 블랙잭
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