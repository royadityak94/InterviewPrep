# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# O(n+n ~ n) time | O(1) space
def smallest_subarray_sum(arr, s):
    ws_start = 0
    current_sum = 0
    bestLengthFound = float('inf')

    for ws_end in range(len(arr)):
        current_sum += arr[ws_end]
        while current_sum >= s:
            bestLengthFound = min(bestLengthFound, (ws_end-ws_start+1))
            current_sum -= arr[ws_start]
            ws_start += 1
        if bestLengthFound == 1:
            break
    return bestLengthFound if bestLengthFound < float('inf') else 0


if __name__ == '__main__':
    print (smallest_subarray_sum([2, 1, 5, 2, 3, 2], 7)) # 2
    print (smallest_subarray_sum([2, 1, 5, 2, 8], 7)) # 1
    print (smallest_subarray_sum([3, 4, 1, 1, 6], 8)) # 3
