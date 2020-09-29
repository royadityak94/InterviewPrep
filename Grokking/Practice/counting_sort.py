from collections import defaultdict

def counting_sort(arr):
    # Time Complexity: ~O(N), Space Complexity: O(N)
    map = [0] * (max(arr)+1)
    # Getting the respective counts
    for ele in arr:
        map[ele] += 1
    # Updating the count array to represent accumulated sum
    for idx in range(1, len(map)):
        map[idx] += map[idx-1]
    new_arr = [None] * map[-1]

    for ele in arr:
        new_arr[map[ele]-1] = ele
        map[ele] -= 1
    return new_arr

def main():
    print (counting_sort([1, 4, 1, 2, 7, 3, 5, 2, 1, 2, 1, 4, 6])) # range - [0, 10]

main()
