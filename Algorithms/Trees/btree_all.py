# Prog 0 : Trying out basic tree implementation - warmup common methods!

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)
    def print_tree(self, mode):
        if mode == 'preorder':
            return self.preorder_traversal(self.root)
        elif mode == 'inorder':
            return self.inorder_traversal(self.root)
        else:
            return self.postorder_traversal(self.root)
    def preorder_traversal(self, root):
        if root is None:
            return
        self.preorder_traversal(root.left)
        print (root.data, end='-')
        self.preorder_traversal(root.right)
    def inorder_traversal(self, root):
        if root is None:
            return
        print (root.data, end='-')
        self.inorder_traversal(root.left)
        self.inorder_traversal(root.right)
    def postorder_traversal(self, root):
        if root is None:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print (root.data, end='-')

    def bfs_traversal(self, root):
        if root is None:
            return
        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)
            print (node.data, end='-')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return

    def dfs_traversal(self, root):
        stack = []
        if root is None:
            return
        stack.append(root)

        while stack:
            node = stack.pop()
            print (node.data, end='-')
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        return

    def reverse_order_bfs_traversal(self, root):
        if root is None:
            return
        stack, queue = [], [root]

        while queue:
            node = queue.pop(0)
            stack.append(node)
            if node.right:
                queue.append(node.right)
            if node.left:
                queue.append(node.left)

        # Iterating over the stack
        while stack:
            node = stack.pop()
            print (node.data, end='-')

        return

    def height_tree(self, root):
        if root is None:
            return -1
        return max(self.height_tree(root.left), self.height_tree(root.right))+1

    def size_tree(self, root):
        if root is None:
            return 0
        queue = [root]
        cnt = 1
        while queue:
            node = queue.pop(0)
            if node.left:
                cnt += 1
                queue.append(node.left)
            if node.right:
                cnt += 1
                queue.append(node.right)
        return cnt

def main():
    tree = BinaryTree(1)
    tree.root.left = Node(2)
    tree.root.right = Node(3)
    tree.root.left.left = Node(4)
    tree.root.left.right = Node(5)
    tree.root.right.left = Node(6)
    tree.root.right.right = Node(7)
    tree.root.right.right.right = Node(11)

    tree.print_tree('preorder')
    print()

    tree.print_tree('inorder')
    print()


    tree.print_tree('postorder')
    print()

    # implementing Level-order traversal (BFS)
    tree.bfs_traversal(tree.root)
    print()

    # implementing DFS
    tree.dfs_traversal(tree.root)
    print()

    # Reverse order BFS traversal
    tree.reverse_order_bfs_traversal(tree.root)
    print()

    # Height of the tree
    print ("Height of Tree = ", tree.height_tree(tree.root))

    # Size of the tree - total nodes
    print ("Size of Tree = ", tree.size_tree(tree.root))
main()
