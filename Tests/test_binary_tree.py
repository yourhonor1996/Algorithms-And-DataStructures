import unittest
from Algorithms_and_Datastrucures.CodeWithMosh_2nd_Review.BinaryTree import BinaryTree


class TestBinrayTree(unittest.TestCase):
    def setUp(self) -> None:
        self.tree = BinaryTree(10)
        self.root = self.tree.root
    
    def test_insert_2(self):
        self.tree.insert(2)
        self.assertEqual(self.root.left, 2)
        
        self.tree.insert(15)
        self.assertEqual(self.root.right, 15)

        self.tree.insert(4)
        self.assertEqual(self.root.left.right, 4)
        
        
        