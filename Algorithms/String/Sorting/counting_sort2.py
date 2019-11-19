class CountingSort():
    def __init__(self, arr):
        self.arr = arr
    def sort(self):
        N = len(self.arr)
        output, count = [0] * N, [0] * (max(self.arr)+1)

        # Count Occurrences
        for i in range(N):
            count[self.arr[i]] += 1
        # Cummulative Sum
        for i in range(1, len(count)):
            count[i] += count[i-1]
        # Shifting each cell right from R-L
        for i in range(len(count)-1, 0, -1):
            count[i] = count[i-1]
        count[0] = 0

        for i in range(N):
            index = count[self.arr[i]]
            output[index] = self.arr[i]
            count[self.arr[i]] += 1
        return output

if __name__ == '__main__':
    arr = [7, 1, 3, 5, 124, 210, 1, 0, 0, 3, 1, 12, 2, 4]
    sorted_arr = CountingSort(arr).sort()
    print (sorted_arr)