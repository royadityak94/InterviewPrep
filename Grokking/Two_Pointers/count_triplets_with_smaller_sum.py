# Python program to count all triplets with sum less than a given target, such that i != j != k

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

def count_triplets_with_smaller_sum(arr, target):
    # Time Complexity: O(NLogN + N**2), Space Complexity: O(N)
    arr.sort() # Runtime: O(NLogN)
    all_triplets = 0

    for idx in range(len(arr)-2):
        target_sum = target - arr[idx]
        left, right = idx+1, len(arr)-1
        current_sum = 0

        while left < right:
            if (arr[left] + arr[right]) < target_sum:
                current_sum += (right - left)
                left += 1
            else:
                right -= 1
        all_triplets += current_sum

    return all_triplets

def find_all_triplets_with_smaller_sum(arr, target):
    # Time Complexity: O(NLogN + N**3), Space Complexity: O(N)
    arr.sort() # O(NLogN)
    triplets = []
    for idx in range(len(arr)-2):
        left, right = idx+1, len(arr)-1

        while left < right:
            if arr[left] + arr[right] < target - arr[idx]:
                for idx_other in range(left, right+1):
                    if arr[idx] != arr[left] != arr[idx_other]:
                        triplets.append([arr[idx], arr[left], arr[idx_other]])

                left += 1
            else:
                right -= 1

    return triplets

def main():
    test(2, count_triplets_with_smaller_sum([-1, 0, 2, 3], 3), "Test - 1 (Count)")
    test(4, count_triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5), "Test - 2 (Count)")
    test([[-1, 0, 2], [-1, 0, 3]], find_all_triplets_with_smaller_sum([-1, 0, 2, 3], 3), "Test - 1 (Find)")
    test([[-1, 1, 2], [-1, 1, 3], [-1, 1, 4], [-1, 2, 3]], find_all_triplets_with_smaller_sum([-1, 4, 2, 1, 3], 5), "Test - 2 (Find)")

main()
