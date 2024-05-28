from datetime import datetime

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self, key, data):
        if self.root is None:
            self.root = Node(key, data)
        else:
            self._insert(self.root, key, data)

    def _insert(self, node, key, data):
        if key < node.key:
            if node.left is None:
                node.left = Node(key, data)
            else:
                self._insert(node.left, key, data)
        elif key > node.key:
            if node.right is None:
                node.right = Node(key, data)
            else:
                self._insert(node.right, key, data)
        else:
            node.data = data

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node

        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            temp = self._min_value_node(node.right)
            node.key = temp.key
            node.data = temp.data
            node.right = self._delete(node.right, temp.key)

        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        elements = []
        self._inorder_traversal(self.root, elements)
        return elements

    def _inorder_traversal(self, node, elements):
        if node:
            self._inorder_traversal(node.left, elements)
            elements.append((node.key, node.data))
            self._inorder_traversal(node.right, elements)

def generate_reservation_key():
    global count
    count += 1
    return datetime.now().strftime("%Y%m%d%H%M%S")+'.'+str(count)


bst = BST()
count = 0
bst.insert(generate_reservation_key(), 'Reservation 1')
bst.insert(generate_reservation_key(), 'Reservation 2')
bst.insert(generate_reservation_key(), 'Reservation 3')

print("Inorder Traversal:", bst.inorder_traversal())

print("Total Resercations :",count)