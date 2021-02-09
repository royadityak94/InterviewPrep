'''
Also called, Convex Hull Jarvis March Problem.
Source: https://leetcode.com/problems/erect-the-fence/ [Tushar: youtube.com/watch?v=Vu84lmMzP2o&list=PLrmLmBdmIlptzAvGVMbeEQvE66ws0PR6a]
There are some trees, where each tree is represented by (x,y) coordinate in a two-dimensional garden.
Your job is to fence the entire garden using the minimum length of rope as it is expensive. The garden is well fenced only if all the trees are enclosed. Your task is to help find the coordinates of trees which are exactly located on the fence perimeter.
'''

class Point:
    def __init__(self, array):
        self.x = array[0]
        self.y = array[1]

# 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
# Returns a positive value, if OAB makes a counter-clockwise turn,
# negative for clockwise turn, and zero if the points are collinear.
def cross_product(point1, point2, point3):
    return ((point1.x - point3.x) * (point2.y - point3.y)) - ((point1.y - point3.y) * (point2.x - point3.x))

def gift_wrapping(coords):
    # Sort the coordinates
    if len(coords) < 2:
        return coords

    for idx in range(len(coords)):
        coords[idx] = Point(coords[idx])

    points = sorted(coords, key = lambda p: (p.x, p.y))
    #print (points)

    # Building lower fences
    lower = []
    for p in points:
        while len(lower) >= 2 and cross_product(lower[-2], lower[-1], p) < 0:
            lower.pop()
        lower += p,

    # Building upper fences
    upper = []
    for p in points[::-1]:
        while len(upper) >= 2 and cross_product(upper[-2], upper[-1], p) < 0:
            upper.pop()
        upper += p,

    return list(map(lambda point: [point.x, point.y], list(set(lower[:-1] + upper[:-1]))))

if __name__ == '__main__':
    ip = [[1,1], [2,2], [2,0], [2,4], [3,3], [4,2]]
    print (gift_wrapping(ip))
