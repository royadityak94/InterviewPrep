
class RadixSort():
    def __init__(self, arr):
        self.arr = arr

    def countingSort(self, exp):
        arr_len = len(self.arr)
        output, count = [0] * arr_len, [0] * 10

        #Create the count array
        for c in range(arr_len):
            index = self.arr[c] / exp
            count[index % 10] += 1
        
        #Putting count back to general range
        for c in range(10):
            count[c] += count[c-1]

        #Creating the output array
        for i in range(arr_len-1, -1, -1):
            index = self.arr[i] / exp
            output[count[index %10] - 1] = self.arr[i]
            count[index%10] -= 1
        
        # Copying over the output array
        for i in range(arr_len):
            self.arr[i] = output[i]

    def sort(self):
        max_number = max(self.arr)
        exp = 1
        while max_number/exp > 0:
            self.countingSort(exp)
            exp *= 10
        return self.arr

if __name__ == '__main__':
    arr = [12, 4, 11, 10, 18, 5, 6, 0]
    sorted_arr = RadixSort(arr).sort()
    print (sorted_arr)