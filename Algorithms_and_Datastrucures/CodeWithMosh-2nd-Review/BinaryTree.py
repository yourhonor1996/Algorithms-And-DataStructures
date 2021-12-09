class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.right_child : Node = None
        self.left_child : Node = None

    def __eq__(self, other: "Node") -> bool:
        if isinstance(other, Node):
            return self.value == other.value
        elif type(other) == 'int':
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
                if current.left_child is None:
                   current.left_child = new_node
                   break
                current = current.left_child 

            else:
                if current.right_child is None:
                   current.right_child = new_node
                   break
                current = current.right_child 

    def find(self):
        pass


tree = BinaryTree()
tree.insert(10)
tree.insert(2)
tree.insert(3)
tree.insert(13)
tree.insert(15)
print('sdf')