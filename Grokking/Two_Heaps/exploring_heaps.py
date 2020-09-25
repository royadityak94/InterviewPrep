from heapq import heappush, heappop, _siftup, _siftdown, heapify
import bisect

def explore(arr):
    minElements = []

    for ele in arr:
        heappush(minElements, ele)

    print (minElements, minElements[0])

    # Index
    # Delete a particular value from hashmap in O(1) time and O(N) time
    ele = 5
    # O(N) time - using heapify
    index = minElements.index(ele)
    minElements[index] = minElements[-1]
    del minElements[-1]
    heapify(minElements) # O(N)

    # O(1) time - using _siftup and _siftdown
    index = minElements.index(ele)
    minElements[index] = minElements[-1]
    del minElements[-1]
    if index < len(minElements):
        _siftup(minElements, index)
        _siftdown(minElements, 0, index)

    index = minElements.index(1)
    print ("idx:", index)
    minElements[index] = minElements[-1]
    print (minElements, minElements[0])
    del minElements[-1]
    print (minElements, minElements[0])

    if index < len(minElements):
        _siftup(minElements, index)
        print ("1, ", minElements)
        _siftdown(minElements, 0, index)
        print ("2, ", minElements)

    print ("F", minElements, minElements[0])


    # Popping out elements
    while minElements:
        popped = heappop(minElements)
        print ("Popped: ", popped)

def main():
    print (explore([8, 1, -2, 4, 5, 7]))

main()
