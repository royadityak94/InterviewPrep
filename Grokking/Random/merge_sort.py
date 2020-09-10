# Python program to implement the merge sort algorithm

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)

class MergeSort:
    def __init__(self, arr):
        self.arr = arr
    def sort(self, reverse=False):
        rev_idx = [1, -1][reverse==True]
        return self.merge_sort(self.arr, rev_idx)
    def merge_sort(self, arr, rev):
        if len(arr) == 1:
            return
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        self.merge_sort(left, rev)
        self.merge_sort(right, rev)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if (left[i] - right[j])*rev < 0:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
        return arr


def main():
    input = [12, 10, 35, 24, 12, 12, 12, 12, 52]
    reverse = False
    test(sorted(input, reverse=reverse), MergeSort(input).sort(reverse))
    reverse = True
    test(sorted(input, reverse=reverse), MergeSort(input).sort(reverse))

main()
