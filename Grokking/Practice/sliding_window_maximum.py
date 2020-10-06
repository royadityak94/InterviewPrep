from collections import deque
def compute_sliding_window_max_naive(arr, k):
    # Time Complexity: O(N*K)
    max_set = []
    for idx in range(len(arr)-k):
        max_set += max(arr[idx:idx+k]),
    return max_set

def compute_sliding_window_max(arr, k):
    # Time Complexity: O(N)
    maximum = deque()
    max_set = []

    for idx, ele in enumerate(arr):
        while maximum and arr[maximum[-1]] <= ele:
            maximum.pop()

        maximum += idx,

        # adjust the in-bounds
        if idx - maximum[0] >= k:
            maximum.popleft()

        # compute the maximum
        if idx+1 > k:
            max_set += arr[maximum[0]],
    return max_set

def main():
    arr, k = [-1, 2, -3, 1, 2, 6, -6, 7, -8, 1, -2 , -1], 3
    #print (compute_sliding_window_max(arr, k), compute_sliding_window_max_naive(arr, k))
    print (compute_sliding_window_max_naive(arr, k))
    print (compute_sliding_window_max(arr, k))

main()
