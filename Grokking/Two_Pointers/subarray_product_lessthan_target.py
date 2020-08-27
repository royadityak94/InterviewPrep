# Find all contiguous array with product less than the target number
# Inp: [2, 5, 3, 10], target=30; Op: [2], [5], [2, 5], [3], [5, 3], [10]
import operator
from functools import reduce

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def subarray_product_lessthan_target(arr, target):
    # Runtime complexity: O(N**3), Space complexity: O(N)
    subarray = []

    for idx in range(len(arr)):
        left, right = idx, len(arr) - 1

        if arr[idx] < target and [arr[idx]] not in subarray:
            subarray.append([arr[idx]])

        while left <= right:
            if reduce(operator.mul, arr[left:right+1]) < target and arr[left:right+1] not in subarray:
                subarray.append(arr[left:right+1])
                left += 1
            else:
                right -= 1
    return subarray

def main():
    op1 = [[2], [2, 5], [5], [5, 3], [3], [10]]
    op2 = [[8], [8, 2], [2], [2, 6], [6], [6, 5], [5]]
    test(op1, subarray_product_lessthan_target([2, 5, 3, 10], 30), "Test - 1")
    test(op2, subarray_product_lessthan_target([8, 2, 6, 5], 50), "Test - 2")

main()
