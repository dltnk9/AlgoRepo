#15439 베라의 패션션

import sys
input = sys.stdin.readline

# 입력 받기
N = int(input().strip())

# 서로 다른 색상의 상의와 하의를 조합하는 경우의 수
result = N * (N - 1)

# 결과 출력
print(result)
