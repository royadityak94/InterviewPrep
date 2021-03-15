'''Line Reflection
Given n points on a 2D plane, find if there is such a line parallel to y-axis that reflect the given points symmetrically, in other words, answer whether or not if there exists a line that after reflecting all points over the given line the set of the original points is the same that the reflected ones.
'''

# O(n) time | O(1) space
def isReflected(points):
    if len(points) < 2:
        return True

    points = set([tuple(point) for point in points])
    mid = (min(x for x, y in points) + max(x for x, y in points))/2

    for x, y in points:
        mirror_x = mid + (mid - x)
        if (mirror_x, y) not in points:
            return False
    return True


if __name__ == '__main__':
    point1 = [[1,1],[-1,1]]
    point2 = [[1,1],[-1,-1]]
    assert isReflected(point1) == True
    assert isReflected(point2) == False
