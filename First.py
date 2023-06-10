def Iterate(n, arr):
    max = 0
    currentlyMax = 0
    for i in range(1,n):
        if arr[i-1] > arr[i]:
            currentlyMax += 1
            if(currentlyMax > max): max = currentlyMax
        else: currentlyMax = 0
    return max
n = int(input())
arr = [int(i) for i in input().split(' ')]
print(Iterate(n,arr))