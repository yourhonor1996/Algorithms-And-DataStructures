from dataclasses import dataclass


class AVL(object):
    default = "default"
    left = "left"
    right = "right"

    class Node(object):
        def __init__(self, data) -> None:
            self.data = data
            self.left: AVL.Node = None
            self.right: AVL.Node = None
            self.height: int = 0

        def __repr__(self) -> str:
            return f"Node={self.data}"

        @property
        def is_leftheavy(self):
            return AVL.balance_factor(self) > 1

        @property
        def is_rightheavy(self):
            return AVL.balance_factor(self) < -1

    def __init__(self, root_data=None) -> None:
        self.root = AVL.Node(root_data)

    @staticmethod
    def get_height(node: "AVL.Node"):
        return node.height if node else -1

    @staticmethod
    def balance_factor(node: "AVL.Node"):
        return AVL.get_height(node.left) - AVL.get_height(node.right) if node else 0

    def insert(self, data):
        self.root = self.__insert(data)

    def __insert(self, data, root: "AVL.Node" = "default"):
        if root == AVL.default:
            root = self.root

        if root is None or root.data is None:
            return AVL.Node(data)

        if data < root.data:
            root.left = self.__insert(data, root.left)
        else:
            root.right = self.__insert(data, root.right)

        AVL.reset_height(root)

        root = AVL.balance(root)

        return root

    @staticmethod
    def rotate(direction: str, root: "AVL.Node"):
        if direction == AVL.left:
            newroot = root.right
            root.right = newroot.left
            newroot.left = root

        elif direction == AVL.right:
            newroot = root.left
            root.left = newroot.right
            newroot.right = root

        AVL.reset_height(root)
        AVL.reset_height(newroot)

        return newroot

    @staticmethod
    def reset_height(node: "AVL.Node"):
        node.height = max(AVL.get_height(node.left), AVL.get_height(node.right)) + 1

    @staticmethod
    def balance(root: "AVL.Node"):
        if root.is_leftheavy:
            if AVL.balance_factor(root.left) < 0:
                root.left = AVL.rotate(AVL.left, root.left)
            return AVL.rotate(AVL.right, root)

        elif root.is_rightheavy:
            if AVL.balance_factor(root.right) > 0:
                root.right = AVL.rotate(AVL.right, root.right)
            return AVL.rotate(AVL.left, root)

        return root


avl = AVL()
avl.insert(10)
avl.insert(20)
avl.insert(30)
avl.insert(15)
avl.insert(40)
avl.insert(9)
avl.insert(50)
avl.insert(60)
avl.insert(70)
avl.insert(25)
avl.insert(100)

# avl.root = avl.rotate(AVL.right, avl.root)
print("done")
