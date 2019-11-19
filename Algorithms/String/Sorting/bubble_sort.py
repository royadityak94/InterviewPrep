class BubbleSort():
    def __init__(self, arr):
        self.arr = arr
    def sort(self):
        N = len(self.arr)

        for i in range(N):
            for j in range(N-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j], self.arr[j+1] = self.arr[j+1], self.arr[j]

        return self.arr

if __name__ == '__main__':
    arr = [7, 1, 3, 5, 124, 210, 1, 0, 0, 3, 1, 12]
    sorted_arr = BubbleSort(arr).sort()
    print (sorted_arr)