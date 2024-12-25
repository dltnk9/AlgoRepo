import sys
input = sys.stdin.readline

# 입력 받기
s = input().strip()

# 서로 다른 부분 문자열을 저장할 집합
substrings = set()

# 모든 부분 문자열을 집합에 추가
for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        substrings.add(s[i:j])

# 결과 출력
print(len(substrings))