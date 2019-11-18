class QuickSort():
    def __init__(self, arr):
        self.arr = arr
    
    def partition(self, low, high):
        i, pivot = low - 1, arr[high]
        for j in range(low, high):
            if self.arr[j] <= pivot:
                i+=1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        return (i+1)
    
    def quickSort(self, low, high):
        if low < high:
            L = self.partition(low, high)
            self.quickSort(low, L-1)
            self.quickSort(L+1, high)
        return self.arr

if __name__ == '__main__':
    arr = [12, 4, 11, 10, 18, 5, 6, 0]
    sorted_arr = QuickSort(arr).quickSort(0, len(arr)-1)
    print (sorted_arr)