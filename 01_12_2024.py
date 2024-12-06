#10988 팰린드롬
a = input()
length = len(a)//2
flag =True

for case in range(length):
    if(a[case] != a[-case-1]):
        flag=False

if(flag ==True):
    print("1")
else:
    print("0")
    
#1157 단어 공부
a = list(input()) 

caseTest = {} 

for case in a:
    case= case.lower()
    if case in caseTest:
        caseTest[case] += 1
    else:
        caseTest[case] = 1  
        
max_value = max(caseTest.values())
max_keys = [key for key, value in caseTest.items() if value == max_value]


if(len(max_keys) != 1):
    print("?")
else:
    print(max_keys[0].upper())
    
#2941 크로아티아 알파벳
a = (input()) 

chunk = ["c=","c-","dz=","d-","lj","nj","s=","z="] # 시력 이슈로 주어진 값 이상하게 넣어버림 30분 낭비

replacedCount=0
for pattern in chunk:
    while pattern in a:
        replacedCount +=1
        a = a.replace(pattern, ' ', 1) # 이 부분, 처음엔 ""로 처리했는데 값이 처리되고나서 앞 뒤 값이 합쳐져서 새로운 크로아티아 처리가 되어버림 -> 공백 추가
a = a.replace(" ", '')
print(len(a)+replacedCount)

#다른 풀이
a = input()
croatia_a = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia_a:
    a = a.replace(i, "*")

print(len(a))

#1316 그룹 단어 체커 (삽질을 너무 했다)
a = int(input())
checksum={}
tempStore =0

for case in range(a):
    x = input()
    isRow = None
    for case in x:
        if case not in checksum: 
            checksum[case] = True  
            isRow = case 
            
        if(checksum[case]==True and isRow != case):
            checksum[case] = False
            
        isRow = case
        
    if any(value == False for value in checksum.values()):
        None
        
    else:
        tempStore += 1
    checksum = {}
    
print(tempStore)
