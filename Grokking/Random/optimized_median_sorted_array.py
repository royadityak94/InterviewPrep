# Source: https://www.youtube.com/watch?v=LPFhl65R7ww


def median_sorted(num1, num2):
    maxValue, minValue = float('inf'), float('-inf')
    n1, n2 = len(num1), len(num2)
    low, high = 0, n1-1

    while low <= high:
        partitionX = low + (high-low)//2
        partitionY = (n1 + n2 + 1)//2 - partitionX

        maxLeftX = num1[partitionX-1] if partitionX else minValue
        minRightX = num1[partitionX] if partitionX else maxValue
        maxLeftY = num2[partitionY-1] if partitionY else minValue
        minRightY = num2[partitionY] if partitionY else maxValue

        if maxLeftX <= minRightY and maxLeftY <= minRightX:
            if not (n1 + n2) % 2:
                return (max(maxLeftX, maxLeftY) + min(minRightX, minRightY))/2
            else:
                return max(maxLeftX, maxLeftY)
        elif maxLeftX > minRightY:
            high = partitionX - 1
        else:
            low = partitionX + 1
    return -1

if __name__ == '__main__':
    print (median_sorted([1, 3, 8, 9, 15], [7, 11, 18, 19, 21, 25])) # Time: O(Log(Min(M, N))), Space: O(1)
