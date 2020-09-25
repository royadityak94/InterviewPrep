
# def find_affected_idx_horizontal(area_map, distance):
#     affected_idxs = []
#
#     for h_, _ in area_map:
#         if distance < h_:



def getMaxArea(w, h, isVertical, distance):
    # Write your code here

    area_map = []

    w_start = h_start = 0

    for idx in range(len(distance)):
        print (h_start, h, w_start, w, distance[idx], isVertical[idx])
        # Horizontal Cut
        if isVertical[idx] == 0 and distance[idx] < h:
            if distance[idx] >= (h-distance[idx]):
                h = distance[idx]
            else:
                h_start = distance[idx]
        if isVertical[idx] == 1 and distance[idx] < w:
            if distance[idx] >= (w-distance[idx]):
                w = distance[idx]
            else:
                w_start = distance[idx]

        area_map += ((h-h_start)*(w-w_start)),
        print (">>>>", h_start, h, w_start, w, distance[idx], isVertical[idx])

    return area_map



def main():

    #print (getMaxArea(2, 2, [0, 1], [1, 1]))
    print (getMaxArea(10, 5, [1, 0, 1, 0, 1], [2, 3, 4, 4, 8]))



main()
