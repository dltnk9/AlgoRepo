# # 구간 합
import sys
input = sys.stdin.readline
suNo, quizNo = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
temp = 0

for i in numbers:
    temp = temp +i
    prefix_sum.append(temp)
    
for i in range(quizNo):
    s, e = map(int, input().split())
    print(prefix_sum[e] - prefix_sum[s-1])
    
    
# 10430
A,B,C= map(int, input().split())

print((A+B)%C)
print(((A%C)+ (B%C))%C)
print((A*B)%C)
print(((A%C)* (B%C))%C)

# 2588 내 풀이
numbers1 = list(map(int, input()))
numbers2 = list(map(int, input()))

print(f"{numbers2[-1]*int(''.join(map(str, numbers1)))}")
print(f"{(numbers2[-2]*int(''.join(map(str, numbers1))))}")
print(f"{(numbers2[-3]*int(''.join(map(str, numbers1))))}")
print(f"{int(''.join(map(str, numbers1)))*int(''.join(map(str, numbers2)))}")

# 블로그 풀이
# map(int, input().split())로 a, b변수를 입력 받고 a를 b의 일의 자리부터 곱하여 출력합니다. 
# 마지막은 a*b연산을 그대로 출력합니다. b를 기본 입력으로 받으면 String 타입으로 저장되는데, String을 한 글자씩 떼어 Int로 변환하고 곱하면 % 연산을 쓰지 않고도 계산이 가능합니다.

a = int(input())
b = input()

a1 = a * int(b[2])
a2 = a * int(b[1])
a3 = a * int(b[0])
a4 = a * int(b)

print (a1, a2, a3, a4, sep='\n')

# 10171

print(r"""
\    /\
 )  ( ')
(  /  )
 \(__)|
""")

# 10172

print("|\_/|")
print("|q p|   /}")
print("( 0 )\"\"\"\\")
print("|\"^\"`    |")
print("||_/=\\\__|")

#1330
a,b = map(int,(input().split()))

if(a>b):
    print(">")
elif (a==b):
    print("==")
else:
    print("<")
    
#9498 파이썬엔 switch case가 없다
    
score = int(input())

if score >= 90 :
    print('A')
elif score >= 80 :
    print('B')
elif score >= 70 :
    print('C')
elif score >= 60 :
    print('D')
else:
    print('F')

# 2753

num = int(input())

if((num%4 == 0 and num %100 != 0) or num%400 ==0):
    print("1")
else:
    print("0")

# 2884 24 0일때 시간을 0으로 바꿔야하는걸 몰라서 애먹음
H,M = map(int, input().split())
tempHour=0
tempMin=0
temp = ((H*60)+M)

# 610
if(temp > 45):
    temp -= 45
    # 565
    tempHour = temp//60
    # 9
    tempMin = temp-(tempHour*60)
    if(tempHour == 24):
        tempHour =0
    
    print(f"{tempHour} {tempMin}")
else:
    temp += 1440
    temp -= 45
    tempHour = temp//60
    tempMin = temp-(tempHour*60)
    if(tempHour == 24):
        tempHour =0
    
    print(f"{tempHour} {tempMin}")

# 2525 틀렸던게, 만약에 시간이 25 이상이면 저 주석처리된 부분은 아무런 역할도 하지 못한다.
# 위에 있는 코드도 마찬가지로 틀린 코드가 된다.

H,M = map(int, input().split())
Time = int(input())
tempHour=0
tempMin=0
temp = ((H*60)+M)+Time


tempHour = temp//60
tempMin = temp-(tempHour*60)

tempHour %= 24
# if(tempHour == 24): 여기 틀림
#     tempHour =0
    
print(f"{tempHour} {tempMin}")

# 2480
a, b, c = map(int, input().split())
if a == b == c:
    print(10000 + a*1000)
elif a == b or a == c:
    print(1000 + a*100)
elif b == c:
    print(1000 + b*100)
else:
    print(max(a, b, c)*100)
    
# 2739 구구단
a = int(input())

for n in range(1, 10, 1):
    print(f"{a} * {n} = {a*n}")
    
#10950 A+B -3
x = int(input())
for num in range(x,0,-1):
    c,d = map(int, input().split())
    print(f"{c+d}")
    

#8393 합
x = int(input())
temp =0
for num in range(x,0,-1):
    temp += num

print(temp)

#25304 영수증
x = int(input())
y = int(input())

temp =0
for num in range(y,0,-1):
    a,b = map(int, input().split())
    temp += a*b
    a=0
    b=0

final = temp

if(x==final):
    print("Yes")
else:
    print("No")
    
    
    
#25314
x = int(input())

for num in range(x,0,-4):

    print("long",end=' ')
print("int")

#15552 input 시간 초과 -> sys.stdin.readline으로 받아야함
import sys

n = int(input())
for i in range(n):
    a, b = map(int, sys.stdin.readline().split())
    print(a+b)
    
#11021
x = int(input())

for n in range(x):
    a,b = map(int,input().split())
    print(f"Case #{n+1}: {a+b}")

#11022
x = int(input())

for n in range(x):
    a,b = map(int,input().split())
    print(f"Case #{n+1}: {a} + {b} = {a+b}")
    
#2438
x = int(input())

for n in range(x):
    for res in range(n+1):
        print("*", end='')
    print()
    
#2439 이거 첫번째 포문에서 초기값 설정 이상하게 해서 한 칸 띄어진 채로 출력이 됨, 이거 조심
x = int(input())

for n in range(1,x+1):
    for res in range(x,n,-1):
        print(" ", end='')
    for resq in range(0,n,+1):
        print("*", end='')
    print()
    
#10952
flag = 0
while(flag==0):
    a,b = map(int,input().split())
    if(a==0 and b==0):
        flag += 1
        break
        
    print(f"{a+b}")    
    
#10951
while True:
    try:
        A, B = map(int, input().split())
        print(A+B)
    except:
        break