from collections import defaultdict

# O(N + N + N ~ N) time | O(N + N ~ N) space
def counting_sort(array):
    spread = max(array) + 1
    count = [0] * spread

    for ele in array:
        count[ele] += 1

    for idx in range(1, len(count)):
        count[idx] += count[idx-1]

    output = [-1] * len(array)
    for ele in array:
        output[count[ele]-1] = ele
        count[ele] -= 1
    return output


def inplace_counting_sort(array):
    spread = max(array) + 1
    count = [0] * spread

    for ele in array:
        count[ele] += 1

    idx = 0
    for s in range(spread):
        for c in range(count[s]):
            array[idx] = s
            idx += 1
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def main():
    print(counting_sort([1, 4, 1, 23, 42, 12, 19, 2, 7, 3, 5, 2]))
    print (counting_sort([1, 4, 61, 1, 2, 7, 3, 5, 59, 2, 1, 2, 1, 4, 6]))
    # in-place sorting
    print(inplace_counting_sort([7, 1, 4, 1, 2, 7, 3, 5, 2]))
    print (inplace_counting_sort([1, 4, 61, 1, 2, 7, 3, 5, 59, 2, 1, 2, 1, 4, 6]))

main()
