from dataclasses import dataclass


class AVLTree(object):
    default = "default"
    left = "left"
    right = "right"

    class Node(object):
        def __init__(self, data) -> None:

            self.data = data
            self.left: AVLTree.Node = None
            self.right: AVLTree.Node = None
            self.height: int = 0
            # self.balance_factor: int = 0

        def __repr__(self) -> str:
            return f"Node={self.data}"

        @staticmethod
        def get_height(node: "AVLTree.Node"):
            return node.height if node else -1

        @staticmethod
        def balance_factor(node: "AVLTree.Node"):
            return AVLTree.Node.get_height(node.left) - AVLTree.Node.get_height(node.right) if node else 0

        @property
        def is_leftheavy(self):
            return AVLTree.Node.balance_factor(self) > 1

        @property
        def is_rightheavy(self):
            return AVLTree.Node.balance_factor(self) < -1

    def __init__(self, root_data=None) -> None:
        self.root = AVLTree.Node(root_data)

    def insert(self, data):
        self.root = self.__insert(data)

    def __insert(self, data, root: "AVLTree.Node" = "default"):

        if root == AVLTree.default:
            root = self.root

        if root is None or root.data is None:
            return AVLTree.Node(data)

        if data < root.data:
            root.left = self.__insert(data, root.left)
        else:
            root.right = self.__insert(data, root.right)

        root.height = max(AVLTree.Node.get_height(root.left), AVLTree.Node.get_height(root.right)) + 1

        if root.is_rightheavy:
            lbf = AVLTree.Node.balance_factor(root.right)
            if lbf > 0:
                # TODO make rotations here
                print(f"right rotation {root.right}")
            print(f"left rotation {root}")

        elif root.is_leftheavy:
            rbf = AVLTree.Node.balance_factor(root.left)
            if rbf < 0:
                # TODO make rotations here
                print(f"left rotation {root.left}")
            print(f"right rotation {root}")

        return root

    # TODO create this method
    # def rotate(self, direction: str, root: "AVLTree.Node"):
    #     if direction == AVLTree.left:
    #         if root.right.left:
    #             root.left = root.right.left
    #         newroot = root.right
    #         newroot.left = root

    #     elif direction == AVLTree.right:
    #         if root.left.right:
    #             root.right = root.left.right
    #         newroot = root.left
    #         newroot.right = root

    #     return newroot


avl = AVLTree()
avl.insert(30)
avl.insert(20)
avl.insert(10)
avl.insert(25)

avl.root = avl.rotate(AVLTree.right, avl.root)
print("done")
