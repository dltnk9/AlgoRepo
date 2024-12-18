#2501 약수 구하기
N,K =map(int,input().split())

divisors = []
for i in range(1, N+1):
    if N % i ==0: #약수를 구할때 이런 식으로 해야함, 나머지 값이 0이면 약수
        divisors.append(i)

if len(divisors) >= K:
    print(divisors[K-1])
else:
    print(0)

#9506 약수들의 합
#딱히 어려운 점은 없었는데, 출력에서 약간 애를 먹었다.
isDone =False

divisors=[]
sumValue =0
while isDone==False:
    
    a = int(input())
    
    if(a==-1):
        isDone=True
        break
    
    for i in range(1, a):
        if a % i ==0:
            divisors.append(i)
    
    for case in divisors:
        sumValue += case
       
    if(sumValue == a):
        print(f"{a} = ",end="")
        for idx , value in enumerate(divisors):
            print(f"{value}",end="")
            if (idx != len(divisors) - 1):
                print(" + ", end="")
        print()
    else:
        print(f"{a} is NOT perfect.")
    sumValue=0
    divisors=[]
    
#1978 소수 찾기
#엄청 어려운건 아니였는데 소수 조건이 생소했다.
n = int(input())
nums = list(map(int, input().split()))
result = 0

for num in nums:
    cnt = 0
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                cnt += 1 #여기서 cnt가 오를경우 소수가 아니라는 증거가 됨

        if cnt == 0:
            result += 1
    
print(result)

#2581 소수
#시간 초과가 떠서 break를 넣어줌 - 시간 초과 통과
#그리고 range에서 b+1을 까먹고 넣지 않음, 실제로는 b-1이 들어가서 최댓값이 계산이 안 되었다
a = int(input())
b = int(input())
result = 0
divisors = []
totalSum = 0
for case in range(a,b+1):
    cnt = 0
    if case > 1:
        for i in range(2, case):
            if case % i == 0:
                cnt += 1 #여기서 cnt가 오를경우 소수가 아니라는 증거가 됨
                break

        if cnt == 0:
            divisors.append(case)

for case in divisors:
    totalSum += case
    
if len(divisors) == 0:
    print(-1)
else:
    print(totalSum)
    print(min(divisors))
    
#11653 소인수분해
#세부 설정을 잊었다, a>1이랑, 2부터 시작해야한다는거
#신기하게 채점 시간이 정말 오래 걸렸다.
a= int(input())

while a>1:
    
    divisors = []
    for i in range(2, a+1):
        if a % i ==0: #약수를 구할때 이런 식으로 해야함, 나머지 값이 0이면 약수
            divisors.append(i)
    
    for el in divisors:
        while a % el == 0:
            a=a/el
            print(el)

#27323 직사각형 , 너무 쉽다
a = int(input())
b = int(input())

print(a*b)

#1085 직사각형에서 탈출 , 쉬웠다
a = list(map(int,input().split()))
valueStore = []

valueStore.append(a[0])
valueStore.append(a[1])

if((a[2]-a[0]) > 0):
    valueStore.append(a[2]-a[0])
    
if((a[3]-a[1]) > 0):
    valueStore.append(a[3]-a[1])
    
print(min(valueStore))

# 3009 네번째 
# +점
from collections import Counter

storeArray=[]
valueX = []
valueY = []
for case in range(3):
    storeArray.append(list(map(int,input().split(" "))))

valueX.append(storeArray[0][0])
valueX.append(storeArray[1][0])
valueX.append(storeArray[2][0])

valueY.append(storeArray[0][1])
valueY.append(storeArray[1][1])
valueY.append(storeArray[2][1])

# 숫자 빈도 계산
counterX = Counter(valueX)
counterY = Counter(valueY)
print(counterX)
print(counterY)
# 가장 적게 등장한 값 찾기
minX = [key for key, count in counterX.items() if count == min(counterX.values())][0]
minY = [key for key, count in counterY.items() if count == min(counterY.values())][0]

print(f"{minX} {minY}")