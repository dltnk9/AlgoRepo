import sys
import math
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())

# 1부터 N까지의 완전 제곱수의 개수 계산
result = int(math.sqrt(N))

# 결과 출력
print(result)