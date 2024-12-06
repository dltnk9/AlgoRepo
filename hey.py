repeat = 9
a = []
maxValue = 0
indexValue = []

for inx in range(repeat):
    a.append(list(map(int,input().split(" "))))

for inx in range(repeat):
    for innerInx in range(repeat):
        if(maxValue <= a[inx][innerInx]):
            maxValue = a[inx][innerInx]
            indexValue = [inx,innerInx]

print(maxValue)
print(f"{indexValue[0]+1} {indexValue[1]+1}")


# print(a)
# print(a)    
# rows = a[0]
# cols = a[1]

# # 이 부분 다시보자
# b = [[0] * cols for _ in range(rows)]
# c = [[0] * cols for _ in range(rows)]


# for case in range(a[0]):
#         b[case] = list(map(int,input().split(" ")))

# for case in range(a[0]):
#     c[case] = list(map(int,input().split(" ")))

# for addCase in range(a[0]):
#     for innerCase in range(a[1]):
#         b[addCase][innerCase] += c[addCase][innerCase]


# for display in range(a[0]):
#     print(" ".join(map(str, b[display]))) #map으로 string 만들어주고 공백으로 조인시키기
    