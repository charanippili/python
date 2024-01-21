def max_goods_picked_up(n, m, grid):
    dp = [[0] * m for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            # Calculate the maximum goods picked for the current cell
            dp[i][j] = grid[i][j]
            if i > 0:
                dp[i][j] += max(dp[i - 1][j], dp[i - 1][max(0, j - 1)], dp[i - 1][min(m - 1, j + 1)])
    
    # Find the maximum value in the last row of the dp table
    max_goods = max(dp[n - 1])
    return max_goods

# Input
t = int(input())
results = []

for _ in range(t):
    n, m = map(int, input().split())
    grid = []
    for _ in range(n):
        row = list(map(int, input().split()))
        grid.append(row)
    
    max_goods = max_goods_picked_up(n, m, grid)
    results.append(max_goods)

# Output
for result in results:
    print(result)
