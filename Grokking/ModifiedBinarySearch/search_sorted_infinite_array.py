import math

class ArrayReader:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        if index >= len(self.arr):
          return math.inf
        return self.arr[index]


def search_in_infinite_array(reader, key):
    # Time Complexity: O(LogN) + O(LogN), Space Complexity: O(1)
    # TODO: Write your code here
    flag = True
    cnt = 1
    start, end = 0, 0
    while flag:
        bound = 2**cnt
        end = start + bound
        if reader.get(end) == math.inf:
            flag = False
            break
        elif reader.get(end) < key:
            start = end
        else:
            break
        cnt += 1

    while (start <= end):
        mid = start + (end-start)//2
        if reader.get(mid) == key:
            return mid+1
        elif reader.get(mid) < key:
            start = mid + 1
        else:
            end = mid -1
    return -1

def main():
    reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
    print(search_in_infinite_array(reader, 28))
    print(search_in_infinite_array(reader, 11))
    reader = ArrayReader([1, 3, 8, 10, 15])
    print(search_in_infinite_array(reader, 15))
    print(search_in_infinite_array(reader, 200))

main()
