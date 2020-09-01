# Given two sorted arrays in descending order, find ‘K’ pairs with the largest sum where each pair consists of numbers from both the arrays.
# Strategy: K-way merge of sorted lists
from heapq import heappush, heappop

def find_k_largest_pairs(nums1, nums2, k):
    # Time Complexity: O(MNLogK) ~ O(K*KlogK) if M, N > K, Space Complexity: O(K)
    minSumHeap = []
    for i in range(min(k, len(nums1))):
        for j in range(min(k, len(nums2))):
            if len(minSumHeap) < k:
                heappush(minSumHeap, (nums1[i]+nums2[j], i, j))
            else:
                if nums1[i]+nums2[j] < minSumHeap[0][0]:
                    break
                else:
                    heappop(minSumHeap)
                    heappush(minSumHeap, (nums1[i]+nums2[j], i, j))

    # Preparing the results
    results = []
    for _, i, j in minSumHeap:
        results.append([nums1[i], nums2[j]])

    return results

def main():
    print (find_k_largest_pairs([9, 8, 2], [6, 3, 1], 3))
    print (find_k_largest_pairs([5, 2, 1], [2, -1], 3))

main()
