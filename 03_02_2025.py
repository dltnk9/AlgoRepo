#1037 약수수
import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
divisors = list(map(int, input().strip().split()))

# 원래 수 계산
original_number = min(divisors) * max(divisors)

# 결과 출력
print(original_number)

#25192 인사성 밝은 곰곰이
def gomgomi(n):
    gomgom = set()
    cnt = 0
    for _ in range(n):
        word = input()

        # ENTER가 아니고, 새로 접속한 사람이 아니면 횟수 증가
        if word != 'ENTER':
            if word not in gomgom:
                cnt += 1
                gomgom.add(word)
        # ENTER이면, 기존에 접속한 회원 정보 초기화
        elif word == 'ENTER':
            gomgom.clear()

    return cnt


print(gomgomi(int(input())))