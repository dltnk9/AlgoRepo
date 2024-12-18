#15894 수학은 체육과목입니다
#너무 쉬웠다.
a = int(input())

print(a*4)

#9063 대지
tempStoreValueX = []
tempStoreValueY = []
A= []
B= []
for case in range(int(input())):
    a,b = map(int,input().split(" "))
    tempStoreValueX.append(a)
    tempStoreValueY.append(b)
    
A.append([min(tempStoreValueX), min(tempStoreValueY)])
B.append([max(tempStoreValueX), max(tempStoreValueY)])
print(f"{(B[0][0]- A[0][0])*(B[0][1]-A[0][1])}")

#10101 삼각형 외우기
#오타나서 틀림
tempValue = []
for case in range(3):
    tempValue.append(int(input()))

if tempValue[0] == tempValue[1] == tempValue[2] == 60:
    print("Equilateral")
elif sum(tempValue) == 180 and (tempValue[0] == tempValue[1] or tempValue[1] == tempValue[2] or tempValue[0] == tempValue[2]):
    print("Isosceles")
elif sum(tempValue) != 180:
    print("Error")
else:
    print("Scalene")
    
#5073 삼각형
#IF문 순서에 유의해야한다 종료조건 넣지 않았을때 EOF에러 났었고
#그 이후에도 삼각형 성립조건을 먼저 검사해야하는데 그러지 않아서 틀림
isEnd = False

while not isEnd:
    tempValue = list(map(int, input().split()))

    # 종료 조건
    if sum(tempValue) == 0:
        isEnd = True
        continue

    # 변의 정렬 (가장 큰 변이 마지막에 오도록)
    tempValue.sort()

    # 삼각형 유효성 검사
    if tempValue[2] >= tempValue[0] + tempValue[1]:
        print("Invalid")
    # Equilateral 조건
    elif tempValue[0] == tempValue[1] == tempValue[2]:
        print("Equilateral")
    # Isosceles 조건
    elif tempValue[0] == tempValue[1] or tempValue[1] == tempValue[2]:
        print("Isosceles")
    # Scalene 조건
    else:
        print("Scalene")