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

