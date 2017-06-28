class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        left = self.left.key if self.left is not None else 'None'
        right = self.right.key if self.right is not None else 'None'
        s = '{{ key: {}, left: {}, left: {} }}'.format(self.key, left, right)
        return s


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

    def put(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self.root = self._put(self.root, key)

    def _put(self, node, key):
        if node is None:
            return Node(key)
        elif key < node.key:
            node.left = self._put(node.left, key)
            if self.height(node.left) - self.height(node.right) == 2:
                if key < node.left.key:
                    node = self.simple_left_rotate(node)
                elif key > node.right.key:
                    node = self.double_left_rotate(node)
        elif key > node.key:
            node.right = self._put(node.right, key)
            if self.height(node.right) - self.height(node.left) == 2:
                if key > node.right.key:
                    node = self.simple_right_rotate(node)
                elif key < node.right.key:
                    node = self.double_right_rotate(node)

        node.height = max(self.height(node.right), self.height(node.left)) + 1
        return node

    def simple_left_rotate(self, node):
        left = node.left
        node.left = left.right
        left.right = node
        node.height = max(self.height(node.right), self.height(node.left)) + 1
        left.height = max(self.height(left.right), self.height(left.left)) + 1
        return left

    def simple_right_rotate(self, node):
        right = node.right
        node.right = right.left
        right.left = node
        node.height = max(self.height(node.left), self.height(node.right)) + 1
        right.height = max(self.height(right.left), self.height(right.right)) + 1
        return right

    def double_left_rotate(self, node):
        node.left = self.simple_right_rotate(node.left)
        return self.simple_left_rotate(node)

    def double_right_rotate(self, node):
        node.right = self.simple_left_rotate(node.right)
        return self.simple_right_rotate(node)

    def traversal(self):
        if self.root is not None:
            self._traversal(self.root)

    def _traversal(self, node):
        print(node.key)
        if node.left is not None:
            self._traversal(node.left)
        if node.right is not None:
            self._traversal(node.right)


def test():
    tree = AVL()
    tree.put('B')
    tree.put('A')
    print('A B')
    tree.traversal()
    tree.put('E')
    print('A B E')
    tree.traversal()
    tree.put('D')
    print('A B E D')
    tree.traversal()
    tree.put('C')
    print('A B C D E')
    tree.traversal()


if __name__ == '__main__':
    test()
