import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())
divisors = list(map(int, input().strip().split()))

# 원래 수 계산
original_number = min(divisors) * max(divisors)

# 결과 출력
print(original_number)