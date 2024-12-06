#25206 너의 평점은
#전공평점이 뭔지 몰라서 헤맴 + 예약어를 쓰고 변수 초기화 안 하고 바로 대입해서 런타임 에러 뜸

def sumSum(score):
    value = 0
    if(score == "A+"):
        value = 4.5
    elif(score == "A0"):
        value = 4.0
    elif(score == "B+"):
        value = 3.5
    elif(score == "B0"):
        value = 3.0
    elif(score == "C+"):
        value = 2.5
    elif(score == "C0"):
        value = 2.0
    elif(score == "D+"):
        value = 1.5
    elif(score == "D0"):
        value = 1.0
    elif(score == "F"):
        value = 0.0
    return value

repeat = 20

a = []
sumCheck = 0
scoreSum = 0
totalValue = 0
for case in range(repeat):
    value = 0
    tempSum = 0
    b = list(input().split(" "))
    if(b[2] != "P"):
        scoreSum += float(b[1])
        value = sumSum(b[2])
        tempSum = float(b[1]) * value
    sumCheck += tempSum
    tempSum = 0

totalValue = sumCheck/scoreSum
print(totalValue)

# 2738 행렬 덧셈

a = list(map(int,input().split(" ")))
rows = a[0]
cols = a[1]

# 이 부분 다시보자
b = [[0] * cols for _ in range(rows)]
c = [[0] * cols for _ in range(rows)]


for case in range(a[0]):
        b[case] = list(map(int,input().split(" ")))

for case in range(a[0]):
    c[case] = list(map(int,input().split(" ")))

for addCase in range(a[0]):
    for innerCase in range(a[1]):
        b[addCase][innerCase] += c[addCase][innerCase]


for display in range(a[0]):
    print(" ".join(map(str, b[display]))) #map으로 string 만들어주고 공백으로 조인시키기
    
#2566 최댓값
repeat = 9
a = []
maxValue = 0
indexValue = []

for inx in range(repeat):
    a.append(list(map(int,input().split(" "))))

for inx in range(repeat):
    for innerInx in range(repeat):
        if(maxValue <= a[inx][innerInx]): #2차원 배열 접근 array[][] - 파이썬에선 이렇게 해야한다
            maxValue = a[inx][innerInx]
            indexValue = [inx,innerInx]

print(maxValue)
print(f"{indexValue[0]+1} {indexValue[1]+1}")