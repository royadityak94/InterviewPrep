# Ref: https://www.educative.io/courses/grokking-the-coding-interview/B6x69OLX4jY
# Python program to compute the maximum capital within a stipulated profit
from heapq import heappop, heappush

def find_maximum_capital(capital, profits, numberOfProjects, initialCapital):
    # Time Complexity: O(NLogN + KLogN), Space Complexity: O(N)
    # TODO: Write your code here
    # Two heaps - minHeap (capital), maxHeap(profit)
    minHeapCapital, maxHeapProfit = [], []
    for idx in range(len(capital)):
        heappush(minHeapCapital, (idx, capital[idx]))

    available_capital = initialCapital
    for _ in range(numberOfProjects):
        while minHeapCapital and minHeapCapital[0][0] <= available_capital:
            i, capital = heappop(minHeapCapital)
            heappush(maxHeapProfit, (-profits[i], i))

        if not maxHeapProfit:
            break
        available_capital += -heappop(maxHeapProfit)[0]

    return available_capital


def main():
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))


main()
