N = int(input())
dp = [0 for _ in range(max(4, N+1))]
dp[2] = 1
dp[3] = 1
for i in range(4, N+1):
    possible = [dp[i-1]]
    if i%2 == 0:
        possible.append(dp[i//2])
    if i%3 == 0:
        possible.append(dp[i//3])
    dp[i] = min(possible) + 1
print(dp[N])
