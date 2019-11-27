class QuickSort():
    def __init__(self, arr):
        self.arr = list(set(arr))
    def partition(self, low, high):
        i, pivot = low-1, self.arr[high]
        for j in range(low, high):
            if self.arr[j] < pivot:
                i += 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        return i+1
    def sort(self, low, high):
        if low < high:
            L = self.partition(low, high)
            self.sort(low, L-1)
            self.sort(L+1, high)
    def compute_sort(self):
        self.sort(0, len(self.arr)-1)
        return self.arr

def compute_LIS(arr):
    arr = QuickSort(arr).compute_sort()
    maximum, ll = 0, []
    for i in  range(len(arr)):
        length, j = 1, arr[i]
        while j + 1 in arr:
            length += 1
            j = j+1
        if length > maximum:
            maximum, ll = length, arr[i:i+length]
    return maximum, ll

if __name__ == '__main__':
    arr = [12, 2, 6, 4, 5, 1, 15, 16, 15, 17, 17, 18, 7, 3, 2, 8, 9, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 32, 31, 33, 34] #[10, 22, 9, 33, 21, 50, 41, 60]  #
    maximum, longest_list = compute_LIS(arr)
    print (maximum, longest_list)