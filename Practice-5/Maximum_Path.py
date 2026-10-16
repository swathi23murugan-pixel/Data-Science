a = [[3, 3], [1, 3], [2, 5], [4, 2], [1, 1]]
rows = len(a)
cols = len(a[0])
dp = [[0] * cols for i in range(rows)]
dp[0][0] = a[0][0]
for i in range(rows):
    for j in range(cols):
        if i == 0 and j == 0:
            continue
        elif i == 0:
            dp[i][j] = dp[i][j - 1] + a[i][j]
        elif j == 0:
            dp[i][j] = dp[i - 1][j] + a[i][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]) + a[i][j]
path = []
i = rows - 1
j = cols - 1
while i >= 0 and j >= 0:
    path.append(a[i][j])
    if i == 0 and j == 0:
        break
    elif i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    elif dp[i - 1][j] > dp[i][j - 1]:
        i -= 1
    else:
        j -= 1
path.reverse()
print("Maximum path sum:", dp[rows - 1][cols - 1])
print("Path:", path)