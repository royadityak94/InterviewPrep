'''
Program to move zeros to end, while preserving the order in constant space
ex: [1, 0, 2, -3, 2, 0, 1, 2, 0, 0, 2, 3, 0, 4, 5] -> [1, 2, -3, 2, 1, 1, 2, 2, 3, 4, 5, 0, 0, 0, 0, 0]
'''

def move_zeros_end(arr):
    # Time: O(N), Space: O(1)
    if not arr:
        return
    left = right = 0
    while right < len(arr):
        if not arr[right]:
            right += 1
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left, right = left+1, right+1
    while left < len(arr):
        arr[left] = 0
        left += 1
    return arr

if __name__ == '__main__':
    print (move_zeros_end([1, 0, 2, -3, 2, 0, 1, 2, 0, 0, 2, 3, 0, 4, 5]))
