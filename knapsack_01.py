n = int(input("Enter number of items: "))

v = list(map(int, input("Enter profits: ").split()))
w = list(map(int, input("Enter weights: ").split()))

W = int(input("Enter knapsack capacity: "))

dp = [[0]*(W+1) for i in range(n+1)]

for i in range(1, n+1):
    for j in range(W+1):
        dp[i][j] = dp[i-1][j]

        if w[i-1] <= j:
            dp[i][j] = max(dp[i][j],
                v[i-1] + dp[i-1][j-w[i-1]])

print("Maximum Profit:", dp[n][W])
