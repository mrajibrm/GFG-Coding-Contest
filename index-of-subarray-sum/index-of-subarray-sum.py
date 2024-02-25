def subArraySum(arr, N, S):
    curr_sum = 0
    start = 0
    end = -1
    for i in range(N):
        curr_sum += arr[i]

        while curr_sum > S:
            curr_sum -= arr[start]
            start += 1

        if curr_sum == S:
            end = i
            break

    if end == -1:
        return [-1]

    return [start+1, end+1]


def main():
    arr1 = [1,2,3,7,5]
    N1 = 5
    S1 = 12
    print(subArraySum(arr1, N1, S1))

    arr2 = [1,2,3,4,5,6,7,8,9,10]
    N2 = 10
    S2 = 15
    print(subArraySum(arr2, N2, S2))

    arr3 = [1, 2, 3, 4]
    N3 = 4
    S3 = 0
    print(subArraySum(arr3, N3, S3))

if __name__ == "__main__":
    main()