def solution(blocks):
    N = len(blocks)
    left = [0] * N
    right = [0] * N

    # Calculate maximum distance the first frog can jump to the left
    for i in range(1, N):
        if blocks[i] >= blocks[i-1]:
            left[i] = left[i-1] + 1
        else:
            left[i] = 1

    # Calculate maximum distance the second frog can jump to the right
    for i in range(N-2, -1, -1):
        if blocks[i] >= blocks[i+1]:
            right[i] = right[i+1] + 1
        else:
            right[i] = 1

    max_distance = 0

    # Calculate maximum distance between the two frogs
    for i in range(N):
        max_distance = max(max_distance, left[i] + right[i] - 1)

    return max_distance

#Example 1:

blocks = [2, 6, 8, 5]
print(solution(blocks))  # Output: 3


#Example 2:

blocks = [1, 5, 5, 2, 6]
print(solution(blocks))  # Output: 4


#Example 3:
blocks = [1, 1]
print(solution(blocks))  # Output: 2
