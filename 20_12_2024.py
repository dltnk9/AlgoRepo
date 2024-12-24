#1436 영화감독 숌
#문제 이해를 처음에 제대로 하질 못 했다.
n = int(input())

count = 0
number = 666

while True:
    if '666' in str(number):
        count += 1
    if count == n:
        print(number)
        break
    number += 1

#2839 설탕 배달
#재밌는 문제였다, 포문을 활용해서 (0 시작 ~ 끝까지) 풀어내는게 참 인상깊었다.
ㄴ
n = int(input())

# 최소 봉지 개수를 찾기 위한 변수 초기화
min_bags = float('inf')

# 5kg 봉지의 개수를 최대한 많이 사용하면서 3kg 봉지로 나머지를 채우는 방법을 탐색
for five_kg in range(n // 5 + 1):
    remaining = n - (five_kg * 5)
    if remaining % 3 == 0:
        three_kg = remaining // 3
        min_bags = min(min_bags, five_kg + three_kg)

# 최소 봉지 개수가 갱신되지 않았다면, 정확하게 나눌 수 없는 경우이므로 -1 출력
if min_bags == float('inf'):
    print(-1)
else:
    print(min_bags)

#리스트 컴프리핸션 연습
result = [num*3 for num in range(10)]
print(result)

result = [num*3 for num in range(10) if num % 2 == 0]
print(result)

#구구단 만들기
result = [x*y for x in range(2,10)
          for y in range(1,10)] 
print(result)

#enumerate() 함수 연습
for i,name in enumerate(['body','foo','bar']):
    print(i,name)
# 결과값 : 0 body
#             1 foo
#             2 bar   