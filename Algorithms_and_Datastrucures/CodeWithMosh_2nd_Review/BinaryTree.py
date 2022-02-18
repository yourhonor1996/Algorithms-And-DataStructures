class Node:
    def __init__(self, value=None) -> None:
        self.value = value
        self.right: Node = None
        self.left: Node = None

    def __eq__(self, other: "Node") -> bool:
        if isinstance(other, Node):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other

    def __repr__(self) -> str:
        return f"Node<{self.value}>"

    @property
    def has_no_childern(self):
        return (self.right is None) and (self.left is None)


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

    def find(self, value: int):
        current = self.root
        while True:
            if current == value:
                return True

            if current is None:
                return False

            if value < current.value:
                current = current.left
            else:
                current = current.right

    def traverse_executer(self, traverse_function, root_node: Node = None):
        if root_node is None:
            root_node = self.root
        results = []
        traverse_function(root_node, results)
        return results

    def traverse_pre_order(self, root: Node, results: list):
        if root is None:
            return

        results.append(root)
        self.traverse_pre_order(root.left, results)
        self.traverse_pre_order(root.right, results)

    def traverse_in_order(self, root: Node, results: list):
        if root is None:
            return

        self.traverse_in_order(root.left, results)
        results.append(root)
        self.traverse_in_order(root.right, results)

    def traverse_post_order(self, root: Node, results: list):
        if root is None:
            return

        self.traverse_post_order(root.left, results)
        self.traverse_post_order(root.right, results)
        results.append(root)

    def do_traverse_pre_order(self):
        return self.traverse_executer(self.traverse_pre_order)

    def do_traverse_in_order(self):
        return self.traverse_executer(self.traverse_in_order)

    def do_traverse_post_order(self):
        return self.traverse_executer(self.traverse_post_order)


tree = BinaryTree()
a = 20
b = a
b = 3
print(a, b)
