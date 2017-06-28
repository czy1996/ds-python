class Node(object):
    def __init__(self, element=-1):
        self.element = element
        self.next = None


"""
不完整的链表实现, 自行补全
"""
class LinkedList(object):
    def __init__(self):
        self.head = None

    # O(1)
    def is_empty(self):
        return self.head is None

    def length(self):
        index = 0
        node = self.head
        while node is not None:
            index += 1
            node = node.next
        return index

    def find(self, element):
        node = self.head
        while node is not None:
            if node.element == element:
                break
            node = node.next
        return node

    def _node_at_index(self, index):
        i = 0
        node = self.head
        while node is not None:
            if i == index:
                return node
            node = node.next
            i += 1
        return None

    def element_at_index(self, index):
        node = self._node_at_index(index)
        return node.element

    # O(n)
    def insert_before_index(self, position, element):
        node = Node(element)
        if position != 0:
            prev = self._node_at_index(position - 1)
            node.next = prev.next
            prev.next = node
        else:
            node.next = self.head
            self.head = node

    # O(n)
    def insert_after_index(self, position, element):
        node = Node(element)
        if not position == self.length() - 1:
            cur = self._node_at_index(position)
            node.next = cur.next
            cur.next = node
        else:
            if self.last_object() is not None:
                self.last_object().next = node
            else:
                self.head = node

    # O(1)
    def first_object(self):
        return self.head

    # O(n)
    def last_object(self):
        node = self.head
        if self.is_empty() is True:
            return None
        while node.next is not None:
            node = node.next
        return node

    # O(n)
    def append(self, node):
        if self.head is None:
            self.head = node
        else:
            last_node = self.last_object()
            last_node.next = node
            # node.front = last_node


if __name__ == '__main__':
    # test()
    a = Node(0)
    b = Node(1)
    c = Node(2)
    l = LinkedList()
    l.append(a)
    l.append(b)
    l.insert_before_index(0, 4)
    print(l.element_at_index(0), l.element_at_index(1), l.element_at_index(2))
