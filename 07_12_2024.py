#10798 세로 읽기
repeat =5
a=[]
for case in range(repeat):
    a.append(list(input()))

max_length = max(len(row) for row in a)
for case in range(max_length):
    for innerCase in range(5):
        if case < len(a[innerCase]):
            print(a[innerCase][case], end='')
            
#2563 색종이
#방향은 맞았는데 코딩을 이상하게 함

# 도화지 크기
canvas = [[0] * 100 for _ in range(100)]

# 색종이 개수 입력
n = int(input())

# 색종이 영역 표시
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x + 10):
        for j in range(y, y + 10):
            canvas[i][j] = 1  # 색종이 영역을 1로 표시

# 색종이가 덮은 넓이 계산
area = sum(sum(row) for row in canvas)
print(area)

#2745 진법 변환
a, b = input().split(" ")  # a는 변환할 값, b는 진법
sumValue = 0
b = int(b)  # 진법 b를 정수로 변환
lengthValue = len(a)  # a의 길이

for i, case in enumerate(a):
    lengthValue -= 1  # 자릿수 감소

    if case.isdigit():  # 숫자인 경우
        sumValue += int(case) * (b ** lengthValue)
    else:  # 알파벳인 경우
        sumValue += (ord(case) - 55) * (b ** lengthValue)

print(sumValue)

#enumerate의 기본 구조
# enumerate(iterable, start=0)
# iterable:

# 반복 가능한 객체(리스트, 문자열, 튜플 등).
# start:

# 인덱스의 시작값 (기본값: 0).
# 반환값:

# 각 반복에서 (인덱스, 값) 형태의 튜플을 반환.

# 응용 예제
# 1. 짝수 인덱스만 처리

# numbers = [10, 20, 30, 40, 50]

# for index, num in enumerate(numbers):
#     if index % 2 == 0:  # 짝수 인덱스일 때만
#         print(index, num)

# 출력:
# 0 10
# 2 30
# 4 50

# 2. 인덱스와 값을 기준으로 딕셔너리 생성

# words = ["a", "b", "c"]

# indexed_dict = {index: value for index, value in enumerate(words)}
# print(indexed_dict)

# 출력:
# {0: 'a', 1: 'b', 2: 'c'}

#11005 진법 변환 2
a, b = map(int, input().split())  # a: 변환할 숫자, b: 진법
sortedValue = []

while a > 0:
    remainder = a % b  # 나머지 계산
    if remainder < 10:  # 0~9는 숫자로
        sortedValue.append(str(remainder))
    else:  # 10 이상은 문자로
        sortedValue.append(chr(remainder - 10 + ord('A')))
    a = a // b  # 몫 갱신

# 결과는 역순으로 출력
sortedValue.reverse()
print(''.join(sortedValue))

#2720 세탁소 사장 동혁
a = int(input())
counter = []
for case in range(a):
    counter.append([0,0,0,0])



for case in range(a):
    remainder = 0
    b = float(input())
    counter[case][0] = b//25
    remainder = b % 25

    counter[case][1] = remainder//10
    remainder = remainder % 10

    counter[case][2] = remainder//5
    remainder = remainder % 5

    counter[case][3] = remainder//1
    remainder = remainder % 1
    
    remainder=0
    
#출력 초과가 뜸 - 리스트에서 변환시키는걸 깜빡함
for case in counter:
    print(' '.join(map(str, map(int, case))))
    
#2903 중앙 이동 알고리즘
#피보나치 수열인줄알고 식을 잘못 세움
#그냥 수열 계산이랑 아주 비슷했다, 
# 격자 크기 k= 2**n + 1, 점의 개수 (2**n + 1)**2
a = int(input())

result =0

result = (2**a+1)**2

print(result)

#2292 벌집
a = int(input())

count = 1  # 중앙 방(1번 방)은 1층
room = 1   # 첫 번째 방 번호

while a > room:
    room += 6 * count  # 각 층마다 6 * count 방이 추가됨
    count += 1         # 층수 증가

print(count)

#1193 분수 찾기 - 감도 못 잡음, 검색해봄

X = int(input())

# 대각선 그룹 찾기
line = 1
while X > line * (line + 1) // 2:
    line += 1

# 그룹의 시작 번호와 위치 계산
start = (line * (line - 1)) // 2 + 1
pos = X - start

# 분수 계산
if line % 2 == 0:  # 짝수 그룹
    numerator = 1 + pos
    denominator = line - pos
else:  # 홀수 그룹
    numerator = line - pos
    denominator = 1 + pos

print(f"{numerator}/{denominator}")

#2869 달팽이는 올라가고싶다
#이 문제는 시간 제한이 0.25초라 반복문을 사용하면 안 된다, 다른 방법을 찾아야해
import math

# 입력 받기
a, b, v = map(int, input().split())

# 올라가는 거리와 내려가는 거리를 고려하여 필요한 날짜 계산
day = math.ceil((v - b) / (a - b))

print(day)

#5086 배수와 약수
isDone =False
while isDone ==False:
    a = list(map(int,input().split(" ")))
    
    if a[0] == 0 and a[1] ==0:
        isDone==True
        break
    if a[0] % a[1] == 0:
        print("multiple")
    elif a[1] % a[0] == 0:
        print("factor")
    else:
        print("neither")
#어렵지 않게 풀었음, 근데 약수 배수 두개 순서 바꿔서 첫 시도에 틀림

