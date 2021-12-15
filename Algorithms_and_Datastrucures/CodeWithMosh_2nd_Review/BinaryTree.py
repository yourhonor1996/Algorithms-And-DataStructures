class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.right : Node = None
        self.left : Node = None

    def __eq__(self, other: "Node") -> bool:
        if isinstance(other, Node):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
    
    def __repr__(self) -> str:
        return f"Node<{self.value}>"
    
    
class BinaryTree:
    def __init__(self, root_value=None) -> None:
        self.root = Node(root_value)

    def insert(self, value):
        if self.root.value is None:
            self.root.value = value
            return
        
        current = self.root
        new_node = Node(value)

        while True:
            if value < current.value:
                if current.left is None:
                   current.left = new_node
                   break
                current = current.left 

            else:
                if current.right is None:
                   current.right = new_node
                   break
                current = current.right 

    def find(self):
        pass


tree = BinaryTree()
tree.insert(10)
tree.insert(2)
tree.insert(3)
tree.insert(13)
tree.insert(15)
print('sdf')