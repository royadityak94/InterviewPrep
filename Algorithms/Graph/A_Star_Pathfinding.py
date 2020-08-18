class Node():
    ''' Node class for the problem space'''
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    
    def __eq__(self, other):
        return self.position == other.position
    

def a_star(maze, start, end):
    ''' Returns a list of tuples as a path from the given start to the given end in the given maze '''
    # Initializing start and end nodes
    start_node = Node(None, start)
    start_node.f = start_node.g = start_node.h = 0
    end_node = Node(None, end)
    end_node.f = end_node.g = end_node.h = 0
    
    # Initializing openList and closedList
    open_list, closed_list = [], []
    
    # Adding the start node
    open_list.append(start_node)
    
    while len(open_list) > 0:
        # Fetch the current Node
        current_node = open_list[0]
        current_idx = 0
        for idx, item in enumerate(open_list):
            if item.f < current_node.f:
                current_node = item
                current_idx = idx
        
        # Pop the current off the open list and add to the closed list
        open_list.pop(current_idx)
        closed_list.append(current_node)
        
        # Check if the goal has been found
        if current_node == end_node:
            # Backtrack to sketh the path from the end_node to the start_node
            path = []
            current = current_node
            while current is not None:
                path.append(current.position)
                current = current.parent
            return path[::-1] # start -> end

        
        # Generate the children
        children = []
        for new_position in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]: # Adjacent Squares
            # Extract node position
            node_position = (current_node.position[0] + new_position[0], 
                             current_node.position[1] + new_position[1])
            
            # Check for the range
            if node_position[0] > (len(maze)-1) or node_position[0] < 0 or node_position[1] > (len(maze[len(maze)-1]) -1) or node_position[1] < 0:
                continue
            
            # Check if the path is clear (non-blocked)
            if maze[node_position[0]][node_position[1]] != 0:
                continue
                
            # Create new node
            new_node = Node(current_node, node_position)
        
            # Append
            children.append(new_node)

        
        # Loop through the children
        for child in children:
            for closed_child in closed_list:
                # Check if the child is not in closed list
                if child == closed_child:
                    continue

            # Generate the f, g, h values
            child.g = current_node.g + 1
            child.h = ((child.position[0] - end_node.position[0])**2) + \
                        ((child.position[1] - end_node.position[1])**2)
            child.f = child.g + child.h

            # Check if the child is not already in the openList
            for open_node in open_list:
                if child == open_node and child.g > open_node.g:
                    continue

            #Add the child to the openList
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