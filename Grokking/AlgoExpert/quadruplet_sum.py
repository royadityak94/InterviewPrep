'''
Quadruplet Pair Sum:
Ex: [7, 6, 4, -1, 1, 2], targetSum=16. O/p -> [[7, 6, 4, -1], [7, 6, 1, 2]]

'''
# O(N^4) time | O(1) space
def quadruplet_sum_naive(arr, targetSum):
    quadruplets = []
    n = len(arr)

    for i in range(n-3):
        for j in range(i+1, n-2):
            for k in range(j+1, n-1):
                for l in range(k+1, n):
                    current = [arr[i], arr[j], arr[k], arr[l]]
                    if sum(current) == targetSum:
                        quadruplets += current,
    return quadruplets

# O(N^3) time | O(1) space
def quadruplet_sum_midoptimized(arr, targetSum):
    arr.sort()
    quadruplets = []
    n = len(arr)

    for i in range(n-3):
        for j in range(i+1, n-2):
            new_sum = targetSum - (arr[i] + arr[j])
            left, right = j+1, n-1

            while left < right:
                current_sum = arr[left] + arr[right]
                if current_sum == new_sum:
                    quadruplets += [arr[i], arr[j], arr[left], arr[right]],
                    break
                elif current_sum < new_sum:
                    left += 1
                else:
                    right -= 1
    return quadruplets

# O(N^2) time | O(N^2) space
def quadruplet_sum_optimized(arr, targetSum):
    allPairSum = {}
    quadruplets = []
    n = len(arr)

    for i in range(1, n):
        for j in range(i+1, n):
            new_target = targetSum - (arr[i] + arr[j])
            if new_target in allPairSum:
                for pair in allPairSum[new_target]:
                    quadruplets += pair + [arr[i], arr[j]],

        for k in range(i):
            current_pair = [arr[k], arr[i]]
            sum_ = sum(current_pair)

            if sum_ in quadruplets:
                allPairSum[sum_] += current_pair,
            else:
                allPairSum[sum_] = current_pair,
    return quadruplets

if __name__ == '__main__':
    expected = [[7, 6, 4, -1], [7, 6, 1, 2]]
    # Naive Way: O(N^4), O(1)
    print ("Naive way")
    assert quadruplet_sum_naive([7, 6, 4, -1, 1, 2], 16) == expected

    # Mid-Optimized Way: O(N^3), O(1) space
    print ("Mid Optimized way")
    assert quadruplet_sum_midoptimized([7, 6, 4, -1, 1, 2], 16) == [[-1, 4, 6, 7], [1, 2, 6, 7]]

    # Optimized Way: O(N^2), O(N^2) space
    print ("Optimized way")
    assert quadruplet_sum_optimized([7, 6, 4, -1, 1, 2], 16) == expected
