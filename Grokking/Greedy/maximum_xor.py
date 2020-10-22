# Source: https://www.hackerrank.com/challenges/maximum-xor/problem
from collections import defaultdict

def maxXor(arr, queries):
    # solve here
    result = []
    cached = defaultdict(int)
    for query in queries:
        observed_max = float('-inf')
        for ele in arr:
            if (query, ele) in cached or (ele, query) in cached:
                computed = max(cached[query, ele], cached[ele, query])
            else:
                computed = query ^ ele
                cached[query, ele] = computed
            observed_max = max(observed_max, computed)
        result += observed_max,
    return result

def maxXor22(arr, queries):
    ans = []
    trie = {}
    k = len(bin(max(arr+queries))) - 2
    for number in ['{:b}'.format(x).zfill(k) for x in arr]:
        node = trie
        for char in number:
            node = node.setdefault(char, {})
    for n in queries:
        node = trie
        s = ''
        for char in'{:b}'.format(n).zfill(k) :
            tmp = str(int(char) ^ 1)
            tmp = tmp if tmp in node else char
            s += tmp
            node = node[tmp]
        ans.append(int(s, 2) ^ n)
    return ans

if __name__ == '__main__':
    print (maxXor([5, 1, 7, 4, 3], [2, 0]))
    print (maxXor([1, 3, 5, 7], [17, 6]))
