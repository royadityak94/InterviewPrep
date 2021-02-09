# O(n) time | O(n/k) space
def find_averages_of_subarrays(k, arr):
    outputs = []
    ws_start = 0
    current_sum = 0
    for ws_end in range(len(arr)):
        current_sum += arr[ws_end]
        if (ws_end-ws_start+1) == k:
            outputs += current_sum/k,
            current_sum -= arr[ws_start]
            ws_start += 1
    return outputs

def main():
    result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
    print("Averages of subarrays of size K: " + str(result))


main()
