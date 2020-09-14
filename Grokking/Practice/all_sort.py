import random

class Sorting:
    def __init__(self, arr):
        self.arr = arr

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
            if left[i] < right[j]:
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

    def partition(self, low, high):
        i, pivot = low-1, self.arr[high]
        for j in range(low, high):
            if self.arr[j] < pivot:
                i+=1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.arr[i+1], self.arr[high] = self.arr[high], self.arr[i+1]
        return (i+1)

    def quick_sort(self, low, high):
        if low < high:
            L = self.partition(low, high)
            self.quick_sort(low, L-1)
            self.quick_sort(L+1, high)
        return

    def selection_sort(self):
        # Main purpose is to put smallest element at the first
        n = len(self.arr)
        for i in range(n):
            for j in range(i, n):
                if self.arr[j] < self.arr[i]:
                    self.arr[j], self.arr[i] = self.arr[i], self.arr[j]
        return

    def bubble_sort(self):
        # Main purpose is to put largest element at the end
        n = len(self.arr)
        for i in range(n):
            for j in range(n-i-1):
                if self.arr[j] > self.arr[j+1]:
                    self.arr[j+1], self.arr[j] = self.arr[j], self.arr[j+1]
        return

    def insertion_sort(self):
        # Same strategy as card sorting, created sorted list to the left, pick number from unsorted list and place it in the sorted list
        n = len(self.arr)
        for i in range(1, n):
            key = self.arr[i]
            j = i-1
            while j >= 0 and key < self.arr[j]:
                self.arr[j+1] = self.arr[j]
                j -= 1
            self.arr[j+1] = key
        return

    def sort(self, type='merge'):
        if 'merge' in type:
            self.merge_sort(self.arr)
        elif 'quick' in type:
            self.quick_sort(0, len(self.arr)-1)
        elif 'selection' in type:
            self.selection_sort()
        elif 'bubble' in type:
            self.bubble_sort()
        elif 'insertion' in type:
            self.insertion_sort()
        else:
            return None
        return self.arr

def main():
    arr = [random.randint(0, 5000) for _ in range(50)]
    random.shuffle(arr)

    sorted_arr_merge = Sorting(arr).sort(type='merge')
    sorted_arr_quick = Sorting(arr).sort(type='quick')
    sorted_arr_selection = Sorting(arr).sort(type='selection')
    sorted_arr_bubble = Sorting(arr).sort(type='bubble')
    sorted_arr_insertion = Sorting(arr).sort(type='insertion')
    list.sort(arr)
    print ("All matched ? ", (sorted_arr_merge==sorted_arr_quick==
        sorted_arr_selection==sorted_arr_bubble==sorted_arr_insertion==arr))

main()
