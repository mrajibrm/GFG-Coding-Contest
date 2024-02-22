def subsequenceCount(s, t):
    mod = 10**9 + 7
    n = len(s)
    m = len(t)

    # Store the count of subsequence of t[:j] in s[:i]
    dist_occ = [[0] * (m+1) for _ in range(n+1)]

    # Initialize the first column with 1 as an empty string is a subsequence of any string
    for i in range(n+1):
        dist_occ[i][0] = 1

    # Fill the matrix using recurrence relation
    for i in range(1, n+1):
        for j in range(1, m+1):
            dist_occ[i][j] = dist_occ[i-1][j]  # Exclude the current character in s

            if s[i - 1] == t[j - 1]:
                dist_occ[i][j] = (dist_occ[i][j] + dist_occ[i-1][j-1]) % mod # Include the current character in s

    return dist_occ[n][m]

def main():
    s1 = "banana"
    t1 = "ban"
    print(subsequenceCount(s1, t1))
    s2 = "geeksforgeeks"
    t2 = "ge"
    print(subsequenceCount(s2, t2))


if __name__ == "__main__":
    main()