def AllPossibleStrings(s):
    def generate_subsequences(index, current, result):
        if index == len(s):
            if current:
                result.append(''.join(current))
            return

        # Include the current character in the subsequence
        generate_subsequences(index + 1, current + [s[index]], result)

        # Exclude the current character from the subsequence
        generate_subsequences(index + 1, current, result)

    result = []
    generate_subsequences(0, [], result)
    result.sort()  # Sorting the result lexicographically
    return result

def main():
    s1 = "abc"
    print(AllPossibleStrings(s1))

    s2 = "aa"
    print(AllPossibleStrings(s2))


if __name__ == "__main__":
    main()

