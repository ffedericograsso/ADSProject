import unittest

from AVL import AVL, TreeNode as AVLNode
from BST import BST, TreeNode as BSTNode
from RBT import RBTree, TreeNode as RBTNode
from Project import Project

#test_project.py contiene unit test per la classe Project, verificando che l'inizializzazione, la creazione di nodi, e le modifiche alla struttura funzionino correttamente. I test coprono sia l'accettazione di nomi di strutture che di classi, e assicurano che vengano sollevate eccezioni per input non validi.
class TestProject(unittest.TestCase):
    #test_accepts_string_structures verifica che la classe Project accetti correttamente i nomi delle strutture come stringhe e che inizializzi gli alberi e le fabbriche di nodi corrispondenti.
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

    #test_accepts_class_structures verifica che la classe Project accetti correttamente le classi delle strutture e che inizializzi gli alberi e le fabbriche di nodi corrispondenti.
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

    #test_create_node_returns_correct_node_type verifica che la funzione create_node della classe Project restituisca un nodo del tipo corretto in base alla struttura attualmente selezionata.
    def test_create_node_returns_correct_node_type(self):
        project = Project("AVL", 10)
        node = project.create_node(7)
        self.assertIsInstance(node, AVLNode)
        self.assertEqual(node.key, 7)

    #test_set_structure_updates_tree_and_factory verifica che la funzione set_structure della classe Project aggiorni correttamente la struttura, l'albero e la fabbrica di nodi quando viene chiamata con un nuovo tipo di struttura.
    def test_set_structure_updates_tree_and_factory(self):
        project = Project("BST", 10)
        self.assertIsInstance(project.tree, BST)

        project.set_structure("RBT")

        self.assertEqual(project.structure_name, "RBT")
        self.assertIsInstance(project.tree, RBTree)
        self.assertIs(project.node_factory, RBTNode)

    #test_set_n_updates_n verifica che la funzione set_n della classe Project aggiorni correttamente il valore di n quando viene chiamata con un nuovo valore.
    def test_set_n_updates_n(self):
        project = Project("BST", 10)
        project.set_n(999)
        self.assertEqual(project.n, 999)

    #test_invalid_structure_raises verifica che la classe Project sollevi un'eccezione ValueError quando viene passato un nome di struttura non valido.
    def test_invalid_structure_raises(self):
        with self.assertRaises(ValueError):
            Project("NOT_A_TREE", 10)

    #test_invalid_n_raises verifica che la classe Project sollevi un'eccezione ValueError quando viene passato un valore non valido per n.
    def test_invalid_n_raises(self):
        with self.assertRaises(ValueError):
            Project("BST", 0)

        with self.assertRaises(ValueError):
            Project("BST", -2)

        with self.assertRaises(ValueError):
            Project("BST", "100")


if __name__ == "__main__":
    unittest.main(verbosity=2)
