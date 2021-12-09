import unittest
from Algorithms_and_Datastrucures.CodeWithMosh_2nd_Review.BinaryTree import BinaryTree


class TestBinrayTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinaryTree(10)
        self.root = self.tree.root
    
    def test_insert(self):
        self.tree.insert(2)
        self.assertEqual(self.root.left_child == 2)