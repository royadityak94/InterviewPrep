# Ref: https://www.educative.io/courses/grokking-the-coding-interview/B6x69OLX4jY
# Python program to compute the maximum capital within a stipulated profit
from heapq import heappop, heappush

def find_maximum_capital(capitals, profits, numProjects, initialCapital):
    minCapitalHeap = []
    maxProfitHeap = []

    for i in range(len(capitals)):
        heappush(minCapitalHeap, (capitals[i], i))

    available_capital = initialCapital
    for _ in range(numProjects):
        while minCapitalHeap and minCapitalHeap[0][0] <= available_capital:
            capital, idx = heappop(minCapitalHeap)
            heappush(maxProfitHeap, (-profits[idx], idx))

        if not maxProfitHeap:
            break

        available_capital += -heappop(maxProfitHeap)[0]
    return available_capital



def main():
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2], [1, 2, 3], 2, 1)))
    print("Maximum capital: " +
        str(find_maximum_capital([0, 1, 2, 3], [1, 2, 3, 5], 3, 0)))

main()
