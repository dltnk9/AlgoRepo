import sys

input = sys.stdin.readline
N = int(input().strip())
list_N = list(map(int, input().split()))

M = int(input().strip())
list_M = list(map(int, input().split()))

list_N.sort()

def binary_search(arr, x):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == x:
            return 1
        
        elif arr[mid] < x:
            left = mid + 1
        
        elif arr[mid] > x:
            right = mid -1

    return 0

for m in list_M:
    print(binary_search(list_N, m), end=' ')

