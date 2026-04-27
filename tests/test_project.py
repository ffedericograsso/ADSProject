import unittest

from AVL import AVL, TreeNode as AVLNode
from BST import BST, TreeNode as BSTNode
from RBT import RBTree, TreeNode as RBTNode
from Project import Project


class TestProject(unittest.TestCase):
    def test_accepts_string_structures(self):
        cases = [
            ("BST", BST, BSTNode),
            ("AVL", AVL, AVLNode),
            ("RBT", RBTree, RBTNode),
        ]

        for structure_name, expected_tree_cls, expected_node_cls in cases:
            with self.subTest(structure=structure_name):
                project = Project(structure_name, 100)
                self.assertEqual(project.structure_name, structure_name)
                self.assertIsInstance(project.tree, expected_tree_cls)
                self.assertIs(project.node_factory, expected_node_cls)

    def test_accepts_class_structures(self):
        cases = [
            (BST, "BST", BST),
            (AVL, "AVL", AVL),
            (RBTree, "RBT", RBTree),
        ]

        for structure_cls, expected_name, expected_tree_cls in cases:
            with self.subTest(structure=structure_cls.__name__):
                project = Project(structure_cls, 50)
                self.assertEqual(project.structure_name, expected_name)
                self.assertIsInstance(project.tree, expected_tree_cls)

    def test_create_node_returns_correct_node_type(self):
        project = Project("AVL", 10)
        node = project.create_node(7)
        self.assertIsInstance(node, AVLNode)
        self.assertEqual(node.key, 7)

    def test_set_structure_updates_tree_and_factory(self):
        project = Project("BST", 10)
        self.assertIsInstance(project.tree, BST)

        project.set_structure("RBT")

        self.assertEqual(project.structure_name, "RBT")
        self.assertIsInstance(project.tree, RBTree)
        self.assertIs(project.node_factory, RBTNode)

    def test_set_n_updates_n(self):
        project = Project("BST", 10)
        project.set_n(999)
        self.assertEqual(project.n, 999)

    def test_invalid_structure_raises(self):
        with self.assertRaises(ValueError):
            Project("NOT_A_TREE", 10)

    def test_invalid_n_raises(self):
        with self.assertRaises(ValueError):
            Project("BST", 0)

        with self.assertRaises(ValueError):
            Project("BST", -2)

        with self.assertRaises(ValueError):
            Project("BST", "100")


if __name__ == "__main__":
    unittest.main(verbosity=2)
