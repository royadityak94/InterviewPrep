# Finding all unique quadraplets summing up to the target

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def search_equivalent_triplets(arr, first, second, target):
    left, right = second+1, len(arr)-1
    new_quadraplets = []

    while left < right:
        curr_quadraplet = [arr[first], arr[second], arr[left], arr[right]]

        if sum(curr_quadraplet) == target:
            new_quadraplets.append(curr_quadraplet)
            left, right = left+1, right - 1
            while left < right and arr[left] == arr[left - 1]:
                left +=  1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1

        elif sum(curr_quadraplet) < target:
            left += 1

        else:
            right -= 1

    return new_quadraplets

def quadraple_sum_to_target(arr, target):
    # Runtime Complexity: O(NLogN + N**3), Space Complexity: O(N)
    arr.sort()
    quadraplets = []

    for idx in range(len(arr)-3):
        if idx > 0 and arr[idx] == arr[idx-1]:
            continue

        for j in range(idx+1, len(arr)-2):
            if j > idx+1 and arr[j] == arr[j-1]:
                continue
            new_quadraplets = search_equivalent_triplets(arr, idx, j, target)
            if len(new_quadraplets) > 0:
                quadraplets.append(*new_quadraplets)

    return quadraplets

def main():
    test([[-3, -1, 1, 4], [-3, 1, 1, 2]], quadraple_sum_to_target([4, 1, 2, -1, 1, -3], 1), "Test - 1")
    test([[-2, 0, 2, 2], [-1, 0, 1, 2]], quadraple_sum_to_target([2, 0, -1, 1, -2, 2], 2), "Test - 2")

main()
