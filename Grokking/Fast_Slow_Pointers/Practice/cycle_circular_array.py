
def find_next_index(arr, is_forward, current):
    direction = arr[current] >= 0
    if direction != is_forward:
        return -1
    next_index = (current + arr[current]) % len(arr)
    if next_index == current:
        return -1
    return next_index

# O(n^2) time | O(1) space
def circular_array_loop_exists(arr):
    for i in range(len(arr)):
        is_forward = arr[i] >= 0
        slow = fast = i
        while True:
            slow = find_next_index(arr, is_forward, slow)
            fast = find_next_index(arr, is_forward, fast)
            if fast != -1:
                fast = find_next_index(arr, is_forward, fast)
            if -1 in (slow, fast) or slow == fast:
                break

        if slow != -1 and slow == fast:
            return True
    return False

def main():
    print(circular_array_loop_exists([1, 2, -1, 2, 2]))
    print(circular_array_loop_exists([2, 2, -1, 2]))
    print(circular_array_loop_exists([2, 1, -1, -2]))


main()
