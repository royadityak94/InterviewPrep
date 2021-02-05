# Print the median of two sorted arrays
from typing import List
def median_sorted(nums1: List[int], nums2: List[int]) -> float:
    n1, n2 = len(nums1), len(nums2)
    if not (n1 or n2):
        return 0
    elif not n1 or not n2:
        arr = nums1 if n1 else nums2
        mid_point = len(arr)//2
        if not len(arr) % 2:
            return sum(arr[mid_point-1:mid_point+1])/2
        else:
            return arr[mid_point]

    i = j = k = 0 # i, j points to num1 and num2, k points to final sorted array
    mid_point = (n1 + n2) // 2

    isEven = True if not (n1+n2) % 2 else False

    while k < mid_point:
        if nums1[i] <= nums2[j]:
            i += 1
        else:
            j += 1
        k += 1

    #print (i, j, k, isEven, mid_point) # , nums1[i], nums2[j]

    if not isEven:
        return min(nums1[i], nums2[j])
    else:
        # if i == j:
        #     return (nums1[i] + nums2[j-1])/2
        if i > j:
            return (nums1[i-1] + nums2[j])/2
        else:
            return (nums1[i] + nums2[j-1])/2


if __name__ == '__main__':
    print (median_sorted([1, 3], [2]))
    print (median_sorted([1, 2], [3, 4]))
    print (median_sorted([0, 0], [0, 0]))
    print (median_sorted([1, 12, 15, 26, 38], [2, 13, 17, 30, 45]))
    print (median_sorted([], [1]))
    print (median_sorted([1], []))
    print (median_sorted([1, 3], [2, 7]))
    print (median_sorted([], [1, 2, 3, 4]))
