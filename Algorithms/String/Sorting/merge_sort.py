class MergeSort():
    def __init__(self, arr):
        self.arr = arr
    def merge(self, low, mid, high):
        temp = [0] * (high - low + 1)
        i, j, k = low, mid+1, 0
        while (i <= mid and j <= high):
            if self.arr[i] <= self.arr[j]:
                temp[k] = self.arr[i]
                k, i = k+1, i+1
            else:
                temp[k] = self.arr[j]
                k, j = k+1, j+1
        while (i <= mid):
            temp[k] = self.arr[i]
            k, i = k+1, i+1
        while j <= high:
            temp[k] = self.arr[j]
            k, j = k+1, j+1
        
        for i_ in range(low, high+1):
            self.arr[i_] = temp[i_ - low]
        
        return self.arr

    def mergeSort(self, start, end):
        if (start < end) :
            mid = (start + end) / 2
            self.mergeSort(start, mid)
            self.mergeSort(mid+1, end)
            self.merge(start, mid, end)
        return self.arr

if __name__ == '__main__':
    arr = [12, 4, 11, 10, 18, 5, 6, 0]
    sorted_arr = MergeSort(arr).mergeSort(0, len(arr)-1)
    print (sorted_arr)
    #print (mergeSort(arr, 0, len(arr)-1))