# Implementation of the path-finding algorithm
class Node:
    def __init__(self, parent, position):
        self.parent = parent
        self.position = position
        self.f = self.g = self.h = 0
    def __eq__(self, other):
        return self.position == other.position

def a_star(maze, start, end):
    # Initialization
    start_node = Node(None, start)
    start_node.f = start_node.g = start_node.h = 0
    end_node = Node(None, end)
    end_node.f = end_node.g = end_node.h = 0
    open_list, closed_list = [], []
    open_list.append(start_node)
    print ("I am heree ....")

    while len(open_list) > 0:

        current_node = open_list[0]
        current_idx = 0
        for idx, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_idx = idx
        # Transfer the least 'f' from open_list to closed_list
        open_list.pop(current_idx)
        closed_list.append(current_node)

        # Check if the end node has been reached
        if current_node == end_node:
            print ("Found the path ...")
            # Backtrack: end->start
            path = []
            present = current_node
            while present is not None:
                path.append(present.position)
                present = present.parent
            return path[::-1]

        # Else: Generate children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
            node_position = (current_node.position[0]+new_position[0], current_node.position[1]+new_position[1])
            # Check validity of the new node position
            if node_position[0] < 0 or node_position[0] > len(maze) - 1 or \
                node_position[1] < 0 or node_position[1] > len(maze) - 1 or \
                maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)

        # Looping through the children
        for child in children:
            if child in closed_list:
                continue
            # Generate: g, h, f
            child.g = current_node.g + 1
            child.h = (child.position[0] - end_node.position[0]) ** 2 + \
                (child.position[1] - end_node.position[1]) ** 2
            child.f = child.g + child.h
            # check if the child is not already in open list
            for open_child in open_list:
                if child == open_child and open_child.g < child.g:
                    continue

            # Else: add to the open list
            open_list.append(child)

if __name__ == '__main__':
    maze = [[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    start =  (0, 0)
    end = (7, 6)
    heurestic_path = a_star(maze, start, end)
    print ("Found Path: ", heurestic_path)
