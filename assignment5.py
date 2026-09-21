def lcs(X, Y):
    m = len(X)
    n = len(Y)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m):
        for j in range(n):
            if X[i] == Y[j]:
                dp[i + 1][j + 1] = dp[i][j] + 1
            else:
                dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

    # Get LCS
    i = m
    j = n
    answer = ""

    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            answer = X[i - 1] + answer
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return answer


X = input("Enter first string: ")
Y = input("Enter second string: ")

answer = lcs(X, Y)

print("LCS:", answer)
print("Length:", len(answer))
