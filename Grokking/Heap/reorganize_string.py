'''
Reorganizing string: Given a string, find if the letters can be rearranged such that, no two similar characters are adjacent to each other.
Return empty string if such alignments are not possible.
Example:
IP{'aab'} = 'aba', IP{'aaab'} = ''
'''
from collections import Counter
from heapq import heapify, heappush, heappop

def reorganize_string(input: str) -> str:
    # Time: O(AlogA + N), Space: O(N + A), A: size of alphabet
    if not str:
        return ''
    resultant, counter_str = [], Counter(input)
    pq = [(-val, key) for key, val in counter_str.items()]
    heapify(pq)
    prev_p = prev_q = None

    while pq:
        p, q = heappop(pq)
        resultant += q,
        if prev_p:
            heappush(pq, (prev_p, prev_q))
        p += 1
        prev_p, prev_q = p, q

    resultant = ''.join(resultant)
    if len(resultant) == len(input):
        return resultant
    return ''

if __name__ == '__main__':
    print (reorganize_string('aab'))
    print (reorganize_string('aaab'))
