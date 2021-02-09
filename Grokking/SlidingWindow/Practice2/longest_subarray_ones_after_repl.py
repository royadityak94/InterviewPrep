from collections import defaultdict

# O(N) time | O(1) space
def length_of_longest_substring(arr, k):
    ws_start = 0
    longestFound = float('-inf')
    maxRepeatingOnes = 0

    for ws_end in range(len(arr)):
        rightMem = arr[ws_end]
        if rightMem == 1:
            maxRepeatingOnes += 1

        while (ws_end - ws_start + 1 - maxRepeatingOnes) > k:
            leftMem = arr[ws_start]
            if leftMem == 1:
                maxRepeatingOnes -= 1
            ws_start += 1
        longestFound = max(longestFound, (ws_end - ws_start + 1))
    return longestFound

if __name__ == '__main__':
    print (length_of_longest_substring([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], 2)) #6
    print (length_of_longest_substring([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], 3)) # 9
