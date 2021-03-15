'''Number of Boomerangs
You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters). Return the number of boomerangs.
'''

def getDistanceBetweenPoints(p1, p2):
    dx = p1[0] - p2[0]
    dy = p1[1] - p2[1]
    return (dx**2 + dy**2)

# O(n^2) time | O(n) space
def numberOfBoomerangs(points):
    boomerangs = 0
    if not points:
        return boomerangs

    for idx1, point1 in enumerate(points):
        distanceMap = {}
        for idx2, point2 in enumerate(points):
            if idx1 == idx2:
                continue
            currentDistance = getDistanceBetweenPoints(point1, point2)
            distanceMap[currentDistance] = 1 + distanceMap.get(currentDistance, 0)

        for _, value in distanceMap.items():
            boomerangs += value * (value - 1)
    return boomerangs

if __name__ == '__main__':
    point1 = [[0,0],[1,0],[2,0]]
    point2 = [[1,1],[2,2],[3,3]]
    point3 = [[1,1]]
    assert numberOfBoomerangs(point1) == 2
    assert numberOfBoomerangs(point2) == 2
    assert numberOfBoomerangs(point3) == 0,
