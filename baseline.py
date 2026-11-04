from itertools import combinations


def longest_cubic_subsequence(sequence):
    n = len(sequence)

    # Try the longest possible lengths first.
    for length in range(n - n % 3, 0, -3):
        block_size = length // 3

        for indices in combinations(range(n), length):
            subsequence = "".join(sequence[i] for i in indices)
            block = subsequence[:block_size]

            if subsequence == block * 3:
                return subsequence

    return ""


sequence = input("Enter a sequence: ")
result = longest_cubic_subsequence(sequence)

print("Longest cubic subsequence:", result)
print("Length:", len(result))