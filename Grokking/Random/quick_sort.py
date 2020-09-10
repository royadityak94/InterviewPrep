# Python program to implement the quick sort algorithm
# Worst case complexity: O(N^2), Works better than merge sort with smaller datasets

def test(expected, output, msg=''):
    if expected == output:
        print ('\033[32m', "Test Case successful: %s" % msg, '\033[0m', sep='')
    else:
        print ('\033[31m', "Failed Test Case: %s" % msg, '\033[0m', sep='')
        print ("Expected = ", expected, ", Output = ", output)


class QuickSort:
    def __init__(self, arr):
        self.arr = arr
    def partition(self, low, high):
        i, pivot = low-1, self.arr[high]
        for j in range(low, high):
            if self.arr[j] < (pivot * self.reverse):
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        return i+1
    def quick_sort(self, low, high):
        if low < high:
            p_idx = self.partition(low, high)
            self.quick_sort(low, p_idx-1)
            self.quick_sort(p_idx+1, high)
        return self.arr
    def sort(self, reverse=False):
        if reverse:
            self.reverse = -1
        else:
            self.reverse = 1
        return self.quick_sort(0, len(self.arr)-1)

def main():
    input = [12, 10, 35, 24, 12, 52]
    output = QuickSort(input).sort()
    test(sorted(input), output)

main()
