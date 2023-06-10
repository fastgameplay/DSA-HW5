def CheckDivide(n, arr):
    totalSum = sum(arr)

    if totalSum % 2 != 0:
        print("NO")
    #Target sum for each half
    target = totalSum // 2
    #possible sums to achieve
    dp = [False] * (target + 1)
    #empty check
    dp[0] = True

    for num in arr:
        #run from target to current and update dp
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
            
    if dp[target]:
        print("YES")
    else:
        print("NO")


n = int(input())
arr = [int(i) for i in input().split(' ')]
CheckDivide(n,arr)