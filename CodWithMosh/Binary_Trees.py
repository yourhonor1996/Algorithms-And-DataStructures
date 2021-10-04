import math


class BinaryTree(object):
    default = "default"

    class Node(object):
        def __init__(self, data) -> None:
            self.data = data
            self.left: BinaryTree.Node = None
            self.right: BinaryTree.Node = None

        def __repr__(self) -> str:
            return f"Node={self.data}"

        @property
        def is_leaf(self):
            return self.left is None and self.right is None

        @staticmethod
        def equals(first: "BinaryTree.Node", second: "BinaryTree.Node") -> bool:
            if first is None and second is None:
                return True

            if first is not None and second is not None:
                return (
                    (first.data == second.data)
                    and BinaryTree.Node.equals(first.left, second.left)
                    and BinaryTree.Node.equals(first.right, second.right)
                )
            return False

    def __init__(self, root_data=None) -> None:
        self.root = BinaryTree.Node(root_data)

    def insert(self, data):
        if self.root is None:
            self.root = BinaryTree.Node(data)
            return
        new_node = BinaryTree.Node(data)
        current = self.root
        while True:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = new_node
                    break
            elif data > current.data:
                if current.right:
                    current = current.right
                else:
                    current.right = new_node
                    break

    def exists(self, data):
        if self.root is None:
            return
        current = self.root
        while current != None:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
        return False

    def traverse_preorder(self, root: "BinaryTree.Node" = "default"):
        if root == BinaryTree.default:
            root = self.root

        if root is None:
            return

        print(root)
        self.traverse_preorder(root.left)
        self.traverse_preorder(root.right)

    def traverse_inorder(self, root: "BinaryTree.Node" = "default"):
        if root == BinaryTree.default:
            root = self.root

        if root is None:
            return

        if root.is_leaf:
            print(root)
            return

        self.traverse_inorder(root.left)
        print(root)
        self.traverse_inorder(root.right)

    def traverse_postorder(self, root: "BinaryTree.Node" = "default"):
        if root == BinaryTree.default:
            root = self.root

        if root is None:
            return
        if root.is_leaf:
            print(root)
            return

        self.traverse_postorder(root.left)
        self.traverse_postorder(root.right)
        print(root)

    def height(self, root: "BinaryTree.Node" = "default"):
        if root == BinaryTree.default:
            root = self.root

        if root is None:
            return -1

        if root.is_leaf:
            return 0

        return 1 + max(self.height(root.left), self.height(root.right))

    def minimum(self, root: "BinaryTree.Node" = "default"):
        if root == BinaryTree.default:
            root = self.root

        if root.is_leaf:
            return root.data

        left = self.minimum(root.left) if root.left else math.inf
        right = self.minimum(root.right) if root.right else math.inf

        return min(min(left, right), root.data)

    def equals(self, other: "BinaryTree") -> bool:
        return BinaryTree.Node.equals(self.root, other.root)

    def is_binarysearchtree(self, root: "BinaryTree.Node" = "default", minimum=None, maximum=None):
        maximum = maximum or math.inf
        minimum = minimum or -math.inf

        if root == BinaryTree.default:
            root = self.root

        if root is None:
            return True

        if root.data < minimum or root.data > maximum:
            return False

        return self.is_binarysearchtree(root.left, minimum, root.data - 1) and self.is_binarysearchtree(
            root.right, root.data + 1, maximum
        )

    def swap_root(self):
        temp = self.root.left
        self.root.left = self.root.right
        self.root.right = temp

    def nodes_at_k_distance(self, distance: int, root: "BinaryTree.Node" = "default", results: list = None):

        if root == BinaryTree.default:
            root = self.root

        if distance == 0:
            results.append(root) if not results is None else print(root)
            return
        else:
            self.nodes_at_k_distance(distance - 1, root.left, results) if root.left else None
            self.nodes_at_k_distance(distance - 1, root.right, results) if root.right else None
            distance -= 1

    def traverse_levelorder(self):
        for i in range(self.height()):
            nodes = []
            self.nodes_at_k_distance(i, results=nodes)
            for node in nodes:
                print(node)


bt = BinaryTree(7)
bt.insert(4)
bt.insert(9)
bt.insert(1)
bt.insert(6)
bt.insert(8)
bt.insert(10)

bt2 = BinaryTree(7)
bt2.insert(4)
bt2.insert(9)
bt2.insert(1)
bt2.insert(6)
bt2.insert(8)
bt2.insert(10)
# bt2.insert(30)
# bt.insert(11)
# print()
# bt.insert(0)
# print(root)
# print(root.left, root.right)
# print(root.left.left, root.left.right)
# print(root.right.left, root.right.right)
# print(bt.find(1))
# bt.traverse_preorder()
# bt.traverse_inorder()
# bt.traverse_postorder()
# print(bt.height)
# print(bt.minimum())
# print(min(0, None))
# print(bt.equals(bt2))
# bt.swap_root()
# print(bt.is_binarysearchtree())
# mylist = []
# bt.nodes_at_k_distance(2, results=mylist)
# print(mylist)
# bt.traverse_levelorder()
print(bt.equals(bt2))