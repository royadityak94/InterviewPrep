# Ref : https://www.geeksforgeeks.org/flood-fill-algorithm

def display_screen(screen, msg):
    print (msg)
    for i in range(len(screen)):
        for j in range(len(screen[0])):
            print (screen[i][j], end=" ")
        print()

def isFillValid(screen, x, y, prevC, newC):
    m, n = len(screen), len(screen[0])
    if x < 0 or x >= m or y < 0 or y >= n or screen[x][y] != prevC or screen[x][y] == newC:
        return False
    return True

def flood_fill(screen, x, y, prevC, newC):
    m, n = len(screen), len(screen[0])
    queue = []
    queue.append([x, y])
    screen[x][y] = newC

    while queue:
        current = queue.pop()
        itrX, itrY = current[0], current[1]

        if isFillValid(screen, itrX-1, itrY, prevC, newC):
            screen[itrX-1][itrY] = newC
            queue.append([itrX-1, itrY])
        if isFillValid(screen, itrX+1, itrY, prevC, newC):
            screen[itrX+1][itrY] = newC
            queue.append([itrX+1, itrY])
        if isFillValid(screen, itrX, itrY-1, prevC, newC):
            screen[itrX][itrY-1] = newC
            queue.append([itrX, itrY-1])
        if isFillValid(screen, itrX, itrY+1, prevC, newC):
            screen[itrX][itrY+1] = newC
            queue.append([itrX, itrY+1])
    return screen

if __name__ == '__main__':
    screen =[ [1, 1, 1, 1, 1, 1, 1, 1],  [1, 1, 1, 1, 1, 1, 0, 0],
    [1, 0, 0, 1, 1, 0, 1, 1],  [1, 2, 2, 2, 2, 0, 1, 0],  [1, 1, 1, 2, 2, 0, 1, 0],
    [1, 1, 1, 2, 2, 2, 2, 0],  [1, 1, 1, 1, 1, 2, 1, 1],  [1, 1, 1, 1, 1, 2, 2, 1]]

    x, y = 4, 4
    prevC = screen[x][y]
    print ("Got prevC as = ", prevC)
    newC = 5

    display_screen(screen, "Displaying screen before flood fill")
    new_screen = flood_fill(screen, x, y, prevC, newC)
    display_screen(new_screen, "Displaying screen after flood fill")
