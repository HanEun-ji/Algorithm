import sys
N = int(sys.stdin.readline())
grape = [0]
for _ in range(N):
    grape.append(int(sys.stdin.readline()))

if N<=2:
    print(sum(grape))
else:
    dp = [0 for _ in range(N+1)]
    dp[1] = grape[1]
    dp[2] = grape[1]+grape[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-1], max(dp[i-2], dp[i-3]+grape[i-1]) + grape[i])

    print(max(dp))