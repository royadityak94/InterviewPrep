# Ref: https://www.educative.io/courses/grokking-the-coding-interview/B6x69OLX4jY
# Python program to compute the maximum capital within a stipulated profit
from heapq import heappop, heappush

# O(NLogN + KLogK) time | O(N) space
def find_maximum_capital(capital, profits, numProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    for i in range(len(capital)):
        heappush(minCapitalHeap, (capital[i], i))

    availableCapital = initialCapital
    for _ in range(numProjects):
        while minCapitalHeap and minCapitalHeap[0][0] <= availableCapital:
            capital, i = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[i], i))

        if not maxProfitHeap:
            break
        availableCapital += -heappop(maxProfitHeap)[0]
    return availableCapital

def main():
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))

main()
