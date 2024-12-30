#28278 스택2
#startswith의 발견
import sys
input = sys.stdin.readline

N = int(input())
stack = []
for _ in range(N):
    command = input().strip()

    if command.startswith('1'):
        _, X = command.split()
        stack.append(int(X))
    elif command == '2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == '3':
        print(len(stack))
    elif command == '4':
        print(1 if not stack else 0)
    elif command == '5':
        if stack:
            print(stack[-1])
        else:
            print(-1)

#10773 제로
import sys
input = sys.stdin.readline

# 입력 받기
K = int(input().strip())

# 스택을 저장할 리스트
stack = []

# 명령어 처리
for _ in range(K):
    number = int(input().strip())
    if number == 0:
        if stack:
            stack.pop()
    else:
        stack.append(number)

# 결과 출력
print(sum(stack))