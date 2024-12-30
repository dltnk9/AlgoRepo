#12789 오키도키 간식드리미
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
students = list(map(int, input().split()))

# 스택과 현재 간식을 받을 순서
stack = []
current = 1

for student in students:
    while stack and stack[-1] == current:
        stack.pop()
        current += 1
    if student == current:
        current += 1
    else:
        stack.append(student)

while stack and stack[-1] == current:
    stack.pop()
    current += 1

if not stack:
    print("Nice")
else:
    print("Sad")
    
#18258 큐2
import sys
from collections import deque
input = sys.stdin.readline

# 큐를 저장할 deque
queue = deque()

# 명령어의 수 입력 받기
N = int(input().strip())

# 명령어 처리
for _ in range(N):
    command = input().strip().split()
    
    if command[0] == "push":
        queue.append(int(command[1]))
    elif command[0] == "pop":
        if queue:
            print(queue.popleft())
        else:
            print(-1)
    elif command[0] == "size":
        print(len(queue))
    elif command[0] == "empty":
        print(1 if not queue else 0)
    elif command[0] == "front":
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif command[0] == "back":
        if queue:
            print(queue[-1])
        else:
            print(-1)

#2164 카드2
import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())

# 큐 초기화
queue = deque(range(1, N + 1))

# 카드 처리
while len(queue) > 1:
    queue.popleft()  # 첫 번째 카드를 버림
    queue.append(queue.popleft())  # 두 번째 카드를 맨 뒤로 옮김

# 결과 출력
print(queue[0])


#11866 요세푸스 문제 0
import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N, K = map(int, input().strip().split())

# 큐 초기화
queue = deque(range(1, N + 1))

# 요세푸스 순열을 저장할 리스트
result = []

# 요세푸스 순열 생성
while queue:
    queue.rotate(-(K-1))  # K-1번 회전하여 K번째 사람이 맨 앞에 오도록 함
    result.append(queue.popleft())  # K번째 사람을 제거하고 결과에 추가

# 결과 출력
print("<" + ", ".join(map(str, result)) + ">")

#28279 덱2
import sys
from collections import deque
input = sys.stdin.readline

# 덱을 저장할 deque
deque = deque()

# 명령어의 수 입력 받기
N = int(input().strip())

# 명령어 처리
for _ in range(N):
    command = input().strip().split()
    
    if command[0] == "1":
        deque.appendleft(int(command[1]))
    elif command[0] == "2":
        deque.append(int(command[1]))
    elif command[0] == "3":
        if deque:
            print(deque.popleft())
        else:
            print(-1)
    elif command[0] == "4":
        if deque:
            print(deque.pop())
        else:
            print(-1)
    elif command[0] == "5":
        print(len(deque))
    elif command[0] == "6":
        print(1 if not deque else 0)
    elif command[0] == "7":
        if deque:
            print(deque[0])
        else:
            print(-1)
    elif command[0] == "8":
        if deque:
            print(deque[-1])
        else:
            print(-1)

#2346 풍선 터뜨리기
import sys
from collections import deque
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
balloons = list(map(int, input().strip().split()))

# 풍선의 위치와 이동 값을 저장할 deque
queue = deque((i + 1, balloons[i]) for i in range(N))

# 결과를 저장할 리스트
result = []

# 풍선 터뜨리기
while queue:
    index, move = queue.popleft()
    result.append(index)
    
    if move > 0:
        queue.rotate(-(move - 1))
    elif move < 0:
        queue.rotate(-move)

# 결과 출력
print(" ".join(map(str, result)))

#24511 queuestack
import sys
from collections import deque
input = sys.stdin.readline


N = int(input())
sequence_A = list(map(int, input().split())) ## queue == 0, stack == 1
sequence_B = list(map(int, input().split())) ## i번 자료구조에 들어있는 원소
M = int(input())                             ## 삽입할 수열의 길이
sequence_C = list(map(int, input().split())) ## 삽입할 수열

## 스택은 무시하고 큐만 deque에 추가하기
queue = deque([])
for i in range(N):
  if sequence_A[i] == 0:
    queue.appendleft(sequence_B[i])
else:
  if queue == []:
    print(*sequence_C)
    sys.exit()

## deque가 하나의 큐 처럼 작동
for i in range(M):
  queue.append(sequence_C[i])
  print(queue.popleft(), end = " ")