#2750 수 정렬하기
#버블정렬
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# 입력 받기
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 버블 정렬 수행
bubble_sort(numbers)

# 결과 출력
for num in numbers:
    print(num)
    
#2587 대표값2
# 버블 정렬 함수 정의
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:  # 앞의 값이 뒤의 값보다 크면 교환
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# 숫자 입력 받기
numbers = [int(input()) for _ in range(5)]

# 평균 계산
average = sum(numbers) // 5

# 버블 정렬로 정렬
bubble_sort(numbers)

# 중앙값 계산
median = numbers[2]  # 정렬된 리스트의 세 번째 값

# 결과 출력
print(average)
print(median)

#25305 두 수 비교하기
#너무 더럽게 풀었다. 그냥 선언할 때 바로 list로 받으면 된다.
a,b=map(int,input().split())
tempStore=[]
getStore=[] 
tempStore.append(list(map(int, input().split()))) #쓰레기 코드
tempStore[0].sort(reverse=True)
for case in range(b):
    getStore.append(tempStore[0][case])

print(getStore.pop())

#-------------------------------------
#깔끔한 코드
a, b = map(int, input().split())
tempStore = list(map(int, input().split()))
tempStore.sort(reverse=True)  # 내림차순 정렬
print(tempStore[b-1])  # 상위 b번째 점수 출력

#2751번 수 정렬하기2
#병합 정렬 구현

#쪼개는 구간, 1이 되면 리턴함, 그 값을 left right에 추가해서 merge 수행행
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

#이 부분이 좀 특이했는데 하나하나씩 앞에 나와있는 숫자를 비교해서 sorted에 넣고 한 쪽이 끝에 다다르면 나머지를 그냥 넣어줌
def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# 입력 받기
n = int(input())
numbers = [int(input()) for _ in range(n)]

# 병합 정렬 수행
sorted_numbers = merge_sort(numbers)

# 결과 출력
for num in sorted_numbers:
    print(num)
    
#시간초과 나옴.
import sys

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    sorted_arr = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1

    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])

    return sorted_arr

# 입력 받기
input = sys.stdin.read
data = input().split()
n = int(data[0])
numbers = list(map(int, data[1:]))

# 병합 정렬 수행
sorted_numbers = merge_sort(numbers)

# 결과 출력
sys.stdout.write('\n'.join(map(str, sorted_numbers)) + '\n')

#10989 수 정렬하기3
#메모리 초과가 걸렸었다.
import sys
input = sys.stdin.readline

#계수정렬 활용
n = int(input())
arr = [0] * (10000 + 1) # 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언

#각 입력값에 해당하는 인덱스의 값 증가
for _ in range(n):
    arr[int(input())] += 1
  
for i in range(len(arr)):
    if arr[i] != 0: #0이 아닌 데이터, 즉 입력받은 데이터들을 출력
        for _ in range(arr[i]):
            print(i)

#1427 소트인사이드
#선택 정렬로 구현현
# 입력 받기
number = input().strip()

# 각 자리 숫자를 리스트로 변환
digits = list(number)

# 선택 정렬을 사용하여 내림차순 정렬
for i in range(len(digits)):
    max_idx = i
    for j in range(i + 1, len(digits)):
        if digits[j] > digits[max_idx]:
            max_idx = j
    # 최대값을 현재 위치로 교환
    digits[i], digits[max_idx] = digits[max_idx], digits[i]

# 결과 출력
print(''.join(digits))

#혹은 그냥 내장함수
# 입력 받기
number = input().strip()

# 각 자리 숫자를 리스트로 변환
digits = list(number)

# 내림차순 정렬
digits.sort(reverse=True)

# 결과 출력
print(''.join(digits))

#11650 좌표 정렬하기
import sys
n=int(sys.stdin.readline())
li=[]
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    li.append([a, b])
li.sort()
for i in li:
    print(i[0], i[1])
    
#1181 단어 정렬
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
words = data[1:]

# 중복 제거 - set으로 중복을 제거한 후에 다시 리스트로 변환함
words = list(set(words))

# 단어를 길이와 사전 순으로 정렬
words.sort(key=lambda x: (len(x), x))

# 결과 출력
for word in words:
    print(word)
    
#10814 나이순 정렬
import sys

input = sys.stdin.read
data = input().split()

n = int(data[0])
members = []

# 회원 정보 입력 받기
index = 1
for i in range(n):
    age = int(data[index])
    name = data[index + 1]
    members.append((age, name, i))  # 나이, 이름, 입력 순서
    index += 2

# 나이순으로 정렬, 나이가 같으면 입력 순서대로 정렬
members.sort(key=lambda x: (x[0], x[2]))

# 결과 출력
for age, name, _ in members:
    print(age, name)
    
#10815 숫자 카드
#즐거운 이진탐색
import sys

input = sys.stdin.readline
N = int(input().strip())
list_N = list(map(int, input().split()))

M = int(input().strip())
list_M = list(map(int, input().split()))

list_N.sort()

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == x:
            return 1
        
        elif arr[mid] < x:
            left = mid + 1
        
        elif arr[mid] > x:
            right = mid -1

    return 0

for m in list_M:
    print(binary_search(list_N, m), end=' ')