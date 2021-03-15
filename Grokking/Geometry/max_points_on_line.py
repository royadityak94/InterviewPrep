'''Max Points on a Line
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.
Source: https://leetcode.com/problems/max-points-on-a-line/
'''

def getGreatestCommonFactor(x, y):
    while True:
        if not x:
            return y
        elif not y:
            return x
        x, y = y, x % y

def getSlopeThroughPoints(p1, p2):
    p1x, p1y = p1
    p2x, p2y = p2
    slope = [1, 0]
    if p1x != p2x:
        xDiff = p1x-p2x
        yDiff = p1y-p2y
        gcd = getGreatestCommonFactor(xDiff, yDiff)
        xDiff //= gcd
        yDiff //= gcd
        slope = [yDiff, xDiff]
    return slope

# O(n^2) time | O(n^2) space
def maxPoints(points):
    maxPointsThroughLine = 1
    for idx1, point1 in enumerate(points):
        slopes = {}
        for idx2 in range(idx1+1, len(points)):
            point2 = points[idx2]
            numerator, denominator = getSlopeThroughPoints(point1, point2)
            slopeKey = str(numerator) + ':' + str(denominator)
            if slopeKey not in slopes:
                slopes[slopeKey] = 1
            slopes[slopeKey] += 1

        maxPointsThroughLine = max(maxPointsThroughLine, max(slopes.values(), default=0))
    return maxPointsThroughLine

if __name__ == '__main__':
    points1 = [[1,1],[2,2],[3,3]]
    points2 = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
    assert maxPoints(points1) == 3
    assert maxPoints(points2) == 4
