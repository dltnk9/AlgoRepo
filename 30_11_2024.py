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