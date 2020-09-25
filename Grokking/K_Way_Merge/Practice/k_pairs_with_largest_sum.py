#Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.
from heapq import heappush, heappop

def k_pairs_largest_sum(l1, l2, k):
    # Time Complexity: O(K.K.logK), Space Complexity: O(K)
    minPairs = []

    for i in range(min(k, len(l1))):
        for j in range(min(k, len(l2))):
            if len(minPairs) < k:
                heappush(minPairs, (l1[i], l2[j]))
            else:
                if (minPairs[0][0]+minPairs[0][1]) < l1[i] + l2[j]:
                    heappop(minPairs)
                    heappush(minPairs, (l1[i], l2[j]))

    return sorted(minPairs, key=lambda x: x[0]+x[1], reverse=True)

def main():
    print (k_pairs_largest_sum([9, 8, 2], [6, 3, 1], 3))
    print (k_pairs_largest_sum([5, 2, 1], [2, -1], 3))

main()
