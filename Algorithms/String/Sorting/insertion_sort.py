class InsertionSort():
    def __init__(self, arr):
        self.arr = arr
    def sort(self):
        N = len(self.arr)

        for i in range(1, N):
            key = self.arr[i]
            j = i-1
            while j>=0 and key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key 

if __name__ == '__main__':
    arr = [7, 1, 3, 5, 124, 210, 1, 0, 0, 3, 1, 12]
    sorted_arr = InsertionSort(arr).sort()
    print (sorted_arr)