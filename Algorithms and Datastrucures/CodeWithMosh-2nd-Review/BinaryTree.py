class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.right_child = Node(None)
        self.left_child = Node(None)

    def __eq__(self, other: "Node") -> bool:
        return self.value == other.value


class BinaryTree:
    def __init__(self, root_value) -> None:
        self.root = Node(root_value)

    def insert(self, value):
        current = self.root

        while True:
            if current.value is None:
                pass
            if value < current.value:
                current = current.left_child
            else:
                current = current.right_child
            
    def find(self):
        pass
    

tree = BinaryTree(10)
tree.insert(2)