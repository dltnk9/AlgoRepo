#10807 개수 세기
n = int(input())
n_list = list(map(int, input().split()))
v = int(input())

print(n_list.count(v))

#10871 X보다 작은 수
N,X = map(int,(input().split()))
A = list(map(int, input().split()))

for num in A:
    if num < X:
        print(num, end=" ") 
        
#10818 최소 최대
X = int(input())
A = list(map(int, input().split()))

print(min(A),end=' ')
print(max(A))

#2562
X =9
A=[]
temp = {"index":0, 
        "value": 0}
for num in range(X):
    tempValue= {"value":int(input()),
                "index": num}
    A.append(tempValue)
    if(temp["value"]<tempValue["value"]):
        temp = tempValue

print(temp["value"])
print(temp["index"]+1)

## 모범답안
num_list = []
for i in range(9) :
    num_list.append(int(input()))  			## num_lst 안에 입력된 값들 차례대로 넣기

print(max(num_list))						## max라는 메소드를 이용해 num_lst 내의 최댓값 출력하기
print(num_list.index(max(num_list))+1)

#10810 공 넣기
q,w = map(int,input().split())
a = []
for storage in range(q):
    a.append(0)
for rep in range(w):
    x,y,z = map(int,input().split())
    for i in range(x-1,y):
        a[i]= z
# print(*a) 리스트 언팩 혹은 아래 코드
print(" ".join(map(str, a)))

#10813 공 바꾸기
q,w = map(int,input().split())
a = []
for storage in range(q):
    a.append(storage+1)
for rep in range(w):
    x,y = map(int,input().split())
    temp = a[x-1]
    a[x-1] = a[y-1] # 이 부분 실수함 할당받는 인덱스 또한 -1처리 해야됨
    a[y-1] = temp
print(*a)

#5597 과제 안 내신 분
temp = [False for _ in range(30)]

for num in range(28):
    b = int(input())
    temp[b-1] = True
    
false_indices = [index+1 for index, value in enumerate(temp) if not value]
print(min(false_indices))
print(max(false_indices))

# enumerate()는 반복 가능한 객체를 다음과 같이 인덱스와 값의 튜플로 반환합니다:
# enumerate(["a", "b", "c"])  # → (0, "a"), (1, "b"), (2, "c")

# fruits = ["apple", "banana", "cherry"]

# for index, value in enumerate(fruits):
#     print(index, value)
    
# 0 apple
# 1 banana
# 2 cherry

#3052 나머지
temp = [0] * 10
checked=[False]*42
count=0
for case in range(10):
    a = int(input())
    temp[case] = a%42
for case in range(10):
    if checked[temp[case]] ==False:
        checked[temp[case]] = True
        count+=1
    
print(count)

#10811 문해력 이슈로 문제를 잘못해석해서 배열 요소를 앞으로 하나씩 미는걸 구현함
a,b = map(int,input().split())
temp = []
for case in range(a):
    temp.append(case+1)
print(temp)
for case in range(b):
    x,y = map(int,input().split())
    if(x==y):
        break
    tempStoreValue=0
    for case in range(y-1, x-2, -1):
        if(tempStoreValue==0):
            tempStoreValue = temp[y-1]
            
        if(case!=x-1):
            cup = 0
            cup = tempStoreValue
            tempStoreValue = temp[case-1]
            temp[case-1] = cup
            
        if(case==x-1):
            temp[y-1]=tempStoreValue

    tempStoreValue=0
print(temp)
#정답
N, M = map(int, input().split())
basket = [i for i in range(1, N+1)]

for i in range(M):
    i,j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp

for i in range(N):
    print(basket[i], end = ' ')
    
#1546 평균
a = int(input())
b = list(map(int, input().split()))

c = max(b)
total=0
for case in range(a):
   b[case]= b[case]/c*100
   total += b[case]


print(total/a)

#27866 문자와 문자열
S = input().strip()
i = int(input()) 

print(S[i - 1])

#2743 단어 길이 재기
S = input().strip()

print(len(S))

#9086 문자열
a = int(input())

for case in range(a):  
    S = input().strip()

    print(f"{S[0]}{S[-1]}")
    
#11654 아스키 코드
char = input().strip()

print(ord(char))

#11720 숫자의 합
a = int(input())
b= input()

temp=0
for case in range(a):
    temp+= int(b[case])
    
print(temp)

#10809 알파벳 찾기
S = input()

for x in 'abcdefghijklmnopqrstuvwxyz':
    print(S.find(x), end = ' ')
# find 함수는 어떤 찾는 문자가 문자열 안에서 첫 번째에 위치한 순서를 숫자로 출력한다.
# 만일 찾는 문자가 문자열 안에 없는 경우에는 -1을 출력하는 함수이다.

#2675 문자열 반복
A = int(input())

for case in range(A):
    x, str = input().split()
    x = int(x)
    
    for case in str: 
        print(case*x,end='') #이미 str 순회중
    print()

#1152 단어의 개수
a = list(input().split())
print(len(a))

#2908 상수
a = list(input().split())
# print(len(a))

ax = list(a[0])
ay = list(a[1])
# print(a[0][0])
axTemp = 0
ayTemp = 0
axTemp = ax[0]
ayTemp = ay[0]
ax[0] = ax[2]
ay[0] = ay[2]
ax[2] = axTemp
ay[2] = ayTemp

print(''.join(max(ay,ax)))

#5622 다이얼
from enum import Enum

class Num(Enum):
    A=B=C=3
    D=E=F=4
    G=H=I=5
    J=K=L=6
    M=N=O=7
    P=Q=R=S=8
    T=U=V=9
    W=X=Y=Z=10
    
a = list(input())

temp=0
for case in range(len(a)):
    if(a[case]==0):
        temp+=11
    elif(a[case]==1):
        temp+=2
    else:
        temp += Num[a[case]].value # Enum 클래스에서 .(dot) 접근은 멤버 이름을 명시적으로 사용할 때만 가능합니다.

print(temp)

#11718 그대로 출력하기
import sys

for line in sys.stdin:
    print(line.strip())
#혹은
# try:
#     while True:
#         line = input()
#         print(line)
# except EOFError:
#     pass

#25083 새싹
print(r"""         ,r'"7
r`-_   ,'  ,/
 \. ". L_r'
   `~\/
      |
      |""")

#3003 킹 퀸 룩 비숍 나이트 폰
a=[1,1,2,2,2,8]

#리스트의 각 요소를 순회하려면 굳이 range()를 사용할 필요가 없습니다. 리스트 자체를 for문에 넣을 수 있습니다:
#리스트의 인덱스와 값을 동시에 다루려면 enumerate()를 사용할 수 있습니다:
x = list(map(int, input().split()))
for case in range(len(a)):
    
    print(a[case]-x[case], end=' ')

#2444 별 찍기 7 하드코딩 해버림
countA =0
countB =1
a = int(input())

countA = a
for case in range(a):
    print(" "*(countA-(case+1)),end='')
    print("*"*countB)
    countB +=2
countB -=2
for case in range(0,a,+1):
    countB -= 2
    print(" "*(case+1),end='')
    print("*"*countB)

# 블로그 풀이
n = int(input())
for i in range(1, n):
    print(' '*(n-i) + '*'*(2*i-1))
for i in range(n, 0, -1):
    print(' '*(n-i) + '*'*(2*i-1))