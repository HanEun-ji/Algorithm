import sys
N = int(sys.stdin.readline())
board = []
for _ in range(N):
    board.append([0]+list(map(int, sys.stdin.readline().split()))+[0])
dp = [[0 for _ in range(i+3)] for i in range(N)]
dp[0][1] = board[0][1]
for i in range(1, N):
    for j in range(1, len(dp[i])-1):
        dp[i][j] = board[i][j] + max(dp[i-1][j-1], dp[i-1][j])
print(max(dp[N-1]))