'''
Quadruplet Pair Sum:
Ex: [7, 6, 4, -1, 1, 2], targetSum=16. O/p -> [[7, 6, 4, -1], [7, 6, 1, 2]]

'''

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






if __name__ == '__main__':
    # Naive Way: O(N^4), O(1) space
    quadruplet_sum_naive([7, 6, 4, -1, 1, 2], 16)


    # Mid-Optimized Way: O(N^3), O(1) space



    # Optimized Way: O(N^2), O(N^2) space
