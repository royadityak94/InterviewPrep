# Source: https://www.hackerrank.com/challenges/angry-children/problem
# Unfairness = max(subarr) - min(subarr)

def maxMin(k, arr):
    # Sorting the subarray
    arr.sort()
    min_unfairness = float('inf')

    for i in range(len(arr)-k+1):
        diff = arr[i+k-1] - arr[i]
        min_unfairness = min(min_unfairness, diff)

    return min_unfairness


if __name__ == '__main__':
    print (maxMin(3, [10, 100, 300, 200, 1000, 20, 30]))
    print (maxMin(4, [200, 100, 40, 1, 2, 3, 4, 10, 20, 30]))
