class QuickSort():
    def __init__(self, arr):
        self.arr = arr
    def partition(self, low, high):
        i, pivot = low-1, self.arr[high]
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        return i+1
    def sort(self, low, high):
        if low < high:
            L = self.partition(low, high)
            self.sort(low, L-1)
            self.sort(L+1, high)
        return self.arr
    def compute_sort(self):
        return self.sort(0, len(self.arr)-1)

class MergeMedian():
    def __init__(self, arr1, arr2):
        self.arr1, self.arr2 = arr1, arr2
    def merge(self):
        l1, l2 = len(self.arr1), len(self.arr2)
        merged = [None] * (l1+l2)
        i, j, k = 0, 0, 0
        while i < l1 and j < l2:
            if self.arr1[i] < self.arr2[j]:
                merged[k] = self.arr1[i]
                i, k = i+1, k+1
            else:
                merged[k] = self.arr2[j]
                j, k = j+1, k+1

        #Complete the rest of the list
        while (i < l1):
            merged[k], i, k  = self.arr1[i], i+1, k+1
        while (j < l2):
            merged[k], j, k  = self.arr2[j], j+1, k+1
        return merged
    def compute_median(self):
        merged = self.merge()
        len_merged = len(merged)
        
        if len_merged % 2 != 0:
            return merged[int(len_merged/2)]
        else:
            return 0.5 * (merged[int(len_merged/2)-1] + merged[int(len_merged/2)])

if __name__ == '__main__':
    arr1 = [23, 37, 1, 5, 7]
    arr2 = [12, 1, 2, 4]

    #Create Sorted Array
    sorted_arr1 = QuickSort(arr1).compute_sort()
    sorted_arr2 = QuickSort(arr2).compute_sort()

    #print (sorted_arr1, sorted_arr2)
    print (MergeMedian(sorted_arr1, sorted_arr2).compute_median())