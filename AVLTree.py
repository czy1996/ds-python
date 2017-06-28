class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0


class AVL:
    def __init__(self):
        self.root = None

    def height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def find(self, key):
        if self.root is None:
            return None
        else:
            return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return None
        elif key < node.key:
            return self._find(node.left, key)
        elif key > node.key:
            return self._find(node.right, key)
        else:
            return node

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, node):
        if node.left is not None:
            return self._find_min(node.left)
        else:
            return node

    def find_max(self):
        if self.root is None:
            return None
        else:
            return self._find_max(self.root)

    def _find_max(self, node):
        if node.right is not None:
            return self._find_max(node)
        else:
            return node
