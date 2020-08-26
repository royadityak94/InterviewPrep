# Python program to square a sorted array

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ("Expected = ", expected, ", Output = ", output)
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')

def find_positive_index(arr):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] >= 0 and arr[mid-1] < 0:
            return mid
        elif arr[mid-1] >= 0:
            right = mid-1
        else:
            left = mid+1

    if arr[0] < 0:
        return len(arr)-1
    else:
        return 0

def square_sorted_array(arr):
    # Time Complexity: O(N), Space Complexity: O(N)
    right = find_positive_index(arr)
    resultant_arr = []
    left = right - 1

    while left > -1 and right < len(arr):
        left_val = arr[left] ** 2
        right_val = arr[right] ** 2

        if len(resultant_arr) == 0:
            if left_val < right_val:
                resultant_arr = [left_val, right_val]
            else:
                resultant_arr = [right_val, left_val]
            left -= 1
            right += 1

        else:
            if left_val < right_val:
                if resultant_arr[len(resultant_arr)-1] <= left_val:
                    resultant_arr.append(left_val)
                    left -= 1
            else:
                if resultant_arr[len(resultant_arr)-1] <= right_val:
                    resultant_arr.append(right_val)
                    right += 1

    while left > -1:
        resultant_arr.append(arr[left]**2)
        left -= 1

    while right < len(arr):
        resultant_arr.append(arr[right]**2)
        right += 1

    return resultant_arr

def square_sorted_array_alternate(arr):
    # Time Complexity: O(N), Space Complexity: O(N)
    resultant_arr = [0 for _ in arr]
    left, right = 0, len(arr) - 1
    placement_idx = right

    while placement_idx > -1:
        left_val = arr[left] ** 2
        right_val = arr[right] ** 2

        if left_val >= right_val:
            resultant_arr[placement_idx] = left_val
            left += 1
        else:
            resultant_arr[placement_idx] = right_val
            right -= 1
        placement_idx -= 1

    return resultant_arr

def main():
    test([0, 1, 4, 4, 9], square_sorted_array([-2, -1, 0, 2, 3]), "Test - 1")
    test([0, 1, 1, 4, 9], square_sorted_array([-3, -1, 0, 1, 2]), "Test - 2")
    test([0, 1, 1, 1, 9], square_sorted_array([-3, -1, -1, -1, 0]), "Test - 3")
    test([1, 1, 4, 4, 9], square_sorted_array([-3, -2, -2, -1, -1]), "Test - 4")
    test([1, 4, 4, 9, 16, 25], square_sorted_array([1, 2, 2, 3, 4, 5]), "Test - 5")
    test([0, 1, 4, 4, 9], square_sorted_array_alternate([-2, -1, 0, 2, 3]), "Test - 1 (Alternate)")
    test([0, 1, 1, 4, 9], square_sorted_array_alternate([-3, -1, 0, 1, 2]), "Test - 2  (Alternate)")
    test([0, 1, 1, 1, 9], square_sorted_array_alternate([-3, -1, -1, -1, 0]), "Test - 3  (Alternate)")
    test([1, 1, 4, 4, 9], square_sorted_array_alternate([-3, -2, -2, -1, -1]), "Test - 4  (Alternate)")
    test([1, 4, 4, 9, 16, 25], square_sorted_array_alternate([1, 2, 2, 3, 4, 5]), "Test - 5  (Alternate)")

main()
