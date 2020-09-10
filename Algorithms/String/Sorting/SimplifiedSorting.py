# Python program to save the implementation of merge and quick sort algorithms
def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)


class Sorting:
    def __init__(self, arr, reverse=False):
        self.arr = arr
        self.rev = [1, -1][reverse==True]
    def merge_sort(self, arr):
        if len(arr) == 1:
            return
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]

        self.merge_sort(left)
        self.merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if (left[i] - right[j])*self.rev < 0:
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

    def partition(self, low, high):
        i, pivot = low-1, self.arr[high]
        for j in range(low, high):
            if (self.arr[j] - pivot)*self.rev < 0:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        return i+1

    def quick_sort(self, low=0, high=None):
        if low < high:
            p_idx = self.partition(low, high)
            self.quick_sort(low, p_idx-1)
            self.quick_sort(p_idx+1, high)
        return self.arr

    def sort(self, type='merge'):
        if type == 'merge':
            return self.merge_sort(self.arr)
        elif type == 'quick':
            return self.quick_sort(high = len(self.arr)-1)
        else:
            return None

def main():
    input = [12, 10, 35, 24, 12, 12, 12, 12, 52]
    # Testing Merge Sort
    reverse = False
    test(sorted(input, reverse=reverse), Sorting(input, reverse).sort(), "Merge Sort Ascending")
    reverse = True
    test(sorted(input, reverse=reverse), Sorting(input, reverse).sort(), "Merge Sort Descending")

    # Testing Quick Sort
    reverse = False
    test(sorted(input, reverse=reverse), Sorting(input, reverse).sort('quick'), "Quick Sort Ascending")
    reverse = True
    test(sorted(input, reverse=reverse), Sorting(input, reverse).sort('quick'), "Quick Sort Descending")

main()
