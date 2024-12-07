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