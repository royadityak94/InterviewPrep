# Source: https://www.hackerrank.coinm/challenges/maximum-xor/problem
from collections import defaultdict

# Efficient soluion: using trie DS
def maxXor(arr, queries):
    result = []
    trie = {}
    k = len(bin(max(arr+queries)))-2

    for number in ['{:3b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for ch in number:
            node = node.setdefault(ch, {})

    for q in queries:
        node = trie
        formed_ = ''

        for ch in '{:b}'.format(q).zfill(k):
            tmp = str(int(ch)^1)
            if tmp not in node:
                tmp = ch
            formed_ += tmp
            node = node[tmp]
        result += int(formed_, 2)^q,
    return result

if __name__ == '__main__':
    print (maxXor([5, 1, 7, 4, 3], [2, 0]))
    print (maxXor([1, 3, 5, 7], [17, 6]))
