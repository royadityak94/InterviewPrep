
from heapq import heappush, heappop, heapify

def reorganize_string(string):
    counter = {}
    for ch in string:
        if ch not in counter:
            counter[ch] = 0
        counter[ch] += 1

    minHeap = [(-value, key) for key, value in counter.items()]
    heapify(minHeap)
    prev_key, prev_value = None, None
    resultant = []

    while minHeap:
        value, key = heappop(minHeap)
        resultant += key,
        if prev_value:
            heappush(minHeap, (prev_value, prev_key))
        prev_key, prev_value = key, value+1

    if len(resultant) == len(string):
        return ''.join(resultant)
    return ''

if __name__ == '__main__':
    print (reorganize_string('aab'))
    print (reorganize_string('aaab'))
    print (reorganize_string('aaabc'))
