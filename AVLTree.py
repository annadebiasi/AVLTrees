"""
PROJECT 5 - AVL Trees
Name:
"""


class TreeNode:
    # DO NOT MODIFY THIS CLASS #
    __slots__ = 'value', 'parent', 'left', 'right', 'height'

    def __init__(self, value, parent=None, left=None, right=None):
        """
        Initialization of a node
        :param value: value stored at the node
        :param parent: the parent node
        :param left: the left child node
        :param right: the right child node
        """
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right
        self.height = 0

    def __eq__(self, other):
        """
        Determine if the two nodes are equal
        :param other: the node being compared to
        :return: true if the nodes are equal, false otherwise
        """
        if type(self) is not type(other):
            return False
        return self.value == other.value

    def __str__(self):
        """String representation of a node by its value"""
        return str(self.value)

    def __repr__(self):
        """String representation of a node by its value"""
        return str(self.value)


class AVLTree:

    def __init__(self):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Initializes an empty Binary Search Tree
        """
        self.root = None
        self.size = 0

    def __eq__(self, other):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Describe equality comparison for BSTs ('==')
        :param other: BST being compared to
        :return: True if equal, False if not equal
        """
        if self.root is None and other.root is None:
            return True

        if self.size != other.size or self.root != other.root:
            return False  # size & root comp

        return self._is_equal(self.root.left, other.root.left) and self._is_equal(self.root.right, other.root.right)

    def _is_equal(self, root1, root2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Checks if rootts are both not None then calls _compare, otherwise checks their equality.
        :param root1: root node of first tree
        :param root2: root node of second tree
        :return: True if equal, False if not
        """
        return self._compare(root1, root2) if root1 and root2 else root1 == root2

    def _compare(self, t1, t2):
        # DO NOT MODIFY THIS FUNCTION #
        """
        Recursively compares two trees, used in __eq__.
        :param t1: root node of first tree
        :param t2: root node of second tree
        :return: True if equal, False if not
        """
        if t1 is None or t2 is None:
            return t1 == t2
        if t1 != t2:
            return False
        return self._compare(t1.left, t2.left) and self._compare(t1.right, t2.right)

    def __str__(self):
        """
        Collects a visual representation of AVL tree
        :return: string of AVL tree
        """
        if not self.root:
            return "Empty AVL Tree..."

        root = self.root
        ans = ""
        bfs_queue = []
        track = {}
        bfs_queue.append((root, 0, root.parent))
        h = AVLTree.height(self.root)

        for i in range(h+1):
            track[i] = []

        while bfs_queue:
            node = bfs_queue.pop(0)
            if node[1] > h:
                break
            track[node[1]].append(node)

            if node[0] is None:
                bfs_queue.append((None, node[1] + 1, None))
                bfs_queue.append((None, node[1] + 1, None))
                continue

            if node[0].left:
                bfs_queue.append((node[0].left, node[1] + 1, node[0]))
            else:
                bfs_queue.append((None,  node[1] + 1, None))

            if node[0].right:
                bfs_queue.append((node[0].right, node[1] + 1, node[0]))
            else:
                bfs_queue.append((None,  node[1] + 1, None))

        spaces = pow(2, h) * 12
        ans += "\n"
        ans += "\t\tVisual Level Order Traversal of AVL Tree - Node (Parent Height)".center(spaces)
        ans += "\n\n"
        for i in range(h+1):
            ans += f"Level {i}: "
            for node in track[i]:
                level = pow(2, i)
                space = int(round(spaces / level))
                if node[0] is None:
                    ans += " " * space
                    continue
                ans += "{} ({} {})".format(node[0], node[2], node[0].height).center(space, " ")
            ans += "\n"
        return ans

    # ------- Implement/Modify the functions below ------- #

    def insert(self, node, value):
        pass

    def remove(self, node, value):
        pass

    @staticmethod
    def height(node):
        pass

    @staticmethod
    def update_height(node):
        pass

    def depth(self, value):
        pass

    def search(self, node, value):
        pass

    def inorder(self, node):
        pass

    def preorder(self, node):
        pass

    def postorder(self, node):
        pass

    def bfs(self):
        pass

    def min(self, node):
        pass

    def max(self, node):
        pass

    def get_size(self):
        pass

    @staticmethod
    def get_balance(node):
        pass

    @staticmethod
    def set_child(parent, child, is_left):
        pass

    @staticmethod
    def replace_child(parent, current_child, new_child):
        pass

    def left_rotate(self, node):
        pass

    def right_rotate(self, node):
        pass

    def rebalance(self, node):
        pass


# ------- Application Problem ------- #
def is_avl_tree(node):
    pass
