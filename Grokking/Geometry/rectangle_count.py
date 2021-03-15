'''Rectangle Count
Write a function returning number of rectangles formed by given coordinates -
we only care about rectangles formed with sides parallel to x, y axes
'''

def getCoordString(coord):
    return '%s-%s' % (coord[0], coord[1])

def getCoordsTable(coords):
    mapper = {}
    for coord in coords:
        mapper[getCoordString(coord)] = True
    return mapper

def isInUpperRight(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return (x2 > x1) and (y2 > y1)

def getRectangleCount(coords, coordTable):
    rectangle_count = 0
    for x1, y1 in coords:
        for x2, y2 in coords:
            if not isInUpperRight((x1, y1), (x2, y2)):
                continue
            upperCoord = getCoordString((x1, y2))
            rightCoord = getCoordString((x2, y1))
            if upperCoord in coordTable and rightCoord in coordTable:
                rectangle_count += 1
    return rectangle_count

def rectangle_count(coords):
    coordTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordTable)

if __name__ == '__main__':
    coord1 = [[0, 0],[0, 1],[1, 1],[1, 0],[2, 1],[2, 0],[3, 1],[3, 0]]
    coord2 = [[0, 0],[0, 1],[1, 1],[1, 0],[2, 1],[2, 0]]
    assert rectangle_count(coord1) == 6
    assert rectangle_count(coord2) == 3
