from random import randint


class node:
    def __init__(self, value=None):
        self.value = value
        self.left_child = None
        self.right_child = None


class binary_search_tree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        self.n = 0
        self.data = list(self.iterator())
        return self

    def __next__(self):
        if self.n < len(self.data):
            old = self.n
            self.n += 1
            return self.data[old].value
        else:
            raise StopIteration

    def insert(self, value):
        if self.root is None:
            self.root = node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.left_child = node(value)
            else:
                self._insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.right_child = node(value)
            else:
                self._insert(value, cur_node.right_child)
        else:
            print("Value already in tree!")

    def check_root(self):
        if self.root is not None:
            return self.root
        return False

    def _iterator(self, cur_node):
        if cur_node is not None:
            yield from self._iterator(cur_node.left_child)
            yield cur_node
            yield from self._iterator(cur_node.right_child)

    def iterator(self):
        root = self.check_root()
        if root is not False:
            return self._iterator(root)

    def print_tree(self):
        print('--' * 20)
        for cur_node in self:
            print(cur_node, end=' | ')
        print()


if __name__ == '__main__':
    tree = binary_search_tree()
    for _ in range(10):
        cur_elem = randint(0, 10000000)
        tree.insert(cur_elem)
    print(list(tree))
    tree.print_tree()
