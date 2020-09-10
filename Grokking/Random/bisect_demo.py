# Python program to check out bisect
import bisect
from itertools import permutations
def main():
    # Insert Complexity: O(N), Search: O(LogN)
    arr = sorted([12, 11, 35, 1, 3, 6, 2, 5])
    print ("Array = ", arr)
    bisect.insort(arr, 21)
    print ("Sorted added 21 = ", arr)
    bisect.insort(arr, 5)
    print ("Sorted added 5 = ", arr)

    print ("Finding indexes of :")
    for ele in arr:
        found_at = bisect.bisect(arr, ele)-1
        print (ele, found_at)

    distinct_elements = set()
    cnt = 0
    for ele in permutations('Aditya', 5):
        formed = "".join(ele)
        distinct_elements.add(formed.lower())
        cnt += 1
    print (len(distinct_elements))

main()
