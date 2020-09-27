
def binary_search(arr, key):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = start + (end-start)//2
        if arr[mid] == key:
            return len(arr)-mid
        elif arr[mid] < key:
            start = mid + 1
        else:
            end = mid - 1
    return -1

def search_bitonic_array(arr, key):
    # Time Complexity: O(Log N), Space Complexity: O(1)
    start, end = 0, len(arr)-1
    flag = False
    while start <= end:
         mid = start + (end-start)//2
         #print (">>> ", start, mid, end)

         if arr[mid] == key:
             return mid
         elif arr[mid-1] < arr[mid] > arr[mid+1]:
             flag = True
             break
         elif arr[mid] < arr[mid+1] and  arr[mid-1] < key :
             start = mid + 1
         else:
             end = mid - 1
    if flag:
        # Search on either side of the array
        right_search = binary_search(arr[mid+1:][::-1], key)
        if right_search != -1:
            return mid + right_search
        return binary_search(arr[:mid], key)
    else:
        return -1

def main():
    print (search_bitonic_array([1, 3, 8, 12, 4, 2], 4))
    print (search_bitonic_array([3, 8, 3, 1, 0, -1, -2], 3))
    print (search_bitonic_array([1, 3, 8, 12], 1))
    print (search_bitonic_array([10, 9, 8, 6, 5, 4, 3, 2, 1], 1))
    # print ('-----------------------------------------')
    print (search_bitonic_array([1, 3, 4, 8, 4, 3], 4))
    print (search_bitonic_array([3, 8, 3, 1], 8))
    print (search_bitonic_array([1, 3, 8, 12], 12))
    print (search_bitonic_array([10, 9, 8], 10))

main()
