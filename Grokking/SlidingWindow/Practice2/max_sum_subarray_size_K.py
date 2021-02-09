# Program to compute the max sum subarray of size K.

# O(n) time | O(1) space
def max_sum_subarray_size_K(arr, k):
    ws_start = 0
    global_best = float('-inf')
    current_sum = 0
    for ws_end in range(len(arr)):
        current_sum += arr[ws_end]

        while (ws_end - ws_start + 1) > k:
            current_sum -= arr[ws_start]
            ws_start += 1
        global_best = max(global_best, current_sum)
    return global_best

def main():
    print ( max_sum_subarray_size_K([2, 1, 5, 1, 3, 2], 3))
    print ( max_sum_subarray_size_K([2, 3, 4, 1, 5], 2))

main()
