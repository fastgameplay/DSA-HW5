def FindSmallestNonNegative(n, arr):
    maxNum = max(arr)
    dp = [False] * (maxNum + 1)
    minimumPossible = 0

    for i in range(n):
        if arr[i] >= 0 and arr[i] <= maxNum:
            dp[arr[i]] = True

        # Find the maximum number among the encountered numbers
        while minimumPossible <= maxNum and dp[minimumPossible]:
            minimumPossible += 1

        print(minimumPossible)



n = int(input())
arr = [int(i) for i in input().split(' ')]

FindSmallestNonNegative(n,arr)
