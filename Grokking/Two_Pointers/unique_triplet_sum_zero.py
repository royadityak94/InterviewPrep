# Python program to find the sum of all unique triplets summing to zero

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')

def unique_triplet_sum_zero(arr):
    # Runtime Complexity: O(NlogN + N**2), Space Complexity: O(N)
    arr.sort() #NlogN
    triplets = []

    for idx in range(len(arr)-1):
        target_sum = -arr[idx]
        left, right = idx+1, len(arr)-1

        while left <= right:
            current_sum = arr[left] + arr[right]
            if target_sum == current_sum:
                triplets.append([arr[idx], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets

def main():
    test([[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]], unique_triplet_sum_zero([-3, 0, 1, 2, -1, 1, -2]), "Test - 1")
    test([[-5, 2, 3], [-2, -1, 3]], unique_triplet_sum_zero([-5, 2, -1, -2, 3]), "Test - 2")

main()
