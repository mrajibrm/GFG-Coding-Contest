def count(n):
    # Create an array to store the number of combinations for each score
    score = [0] * (n + 1)

    # There is one way to score 0 (no move)
    score[0] = 1

    # Iterate through all possivle moves and update score
    for move in [3, 5, 10]:
        for i in range(move, n+1):
            score[i] += score[i-move]

    return score[n]


def main():
    n1 = 10
    n2 = 20
    print(count(n1))
    print(count(n2))


if __name__ == "__main__":
    main()