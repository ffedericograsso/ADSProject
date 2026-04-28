from BST import BST as SimpleBST, TreeNode as BSTNode
from AVL import AVL, TreeNode as AVLNode
from RBT import RBTree, TreeNode as RBTNode

# Questa classe funge da centro di controllo e intermediario tra le strutture dati e i file di esperimento

class Project:
	def __init__(self, structure, n):
		self.structure_name = self._normalize_structure(structure)
		self.n = self._validate_n(n)
		self.tree = self._create_tree()
		self.node_factory = self._get_node_factory()

	# Assicura che i dati in input siano corretti
	def _normalize_structure(self, structure):
		if isinstance(structure, str):
			name = structure.strip().upper()
			if name in {"BST", "SIMPLEBST", "SIMPLE_BST"}:
				return "BST"
			if name == "AVL":
				return "AVL"
			if name in {"RBT", "RBTREE", "RBTREE", "RED_BLACK_TREE"}:
				return "RBT"
		elif structure in {SimpleBST, AVL, RBTree}:
			if structure is SimpleBST:
				return "BST"
			if structure is AVL:
				return "AVL"
			if structure is RBTree:
				return "RBT"

		raise ValueError("La struttura dati può essere solamente BST, AVL o RBT")

	# Si assicura che il valore n sia un intero strettamente positivo
	def _validate_n(self, n):
		if not isinstance(n, int) or n <= 0:
			raise ValueError("n deve essere un intero positivo")
		return n

	# Crea gli alberi in base al nome della struttura
	def _create_tree(self):
		if self.structure_name == "BST":
			return SimpleBST()
		if self.structure_name == "AVL":
			return AVL()
		return RBTree()

	def _get_node_factory(self):
		if self.structure_name == "BST":
			return BSTNode
		if self.structure_name == "AVL":
			return AVLNode
		return RBTNode

	def create_node(self, key):
		return self.node_factory(key)

	def set_structure(self, structure):
		self.structure_name = self._normalize_structure(structure)
		self.tree = self._create_tree()
		self.node_factory = self._get_node_factory()

	def set_n(self, n):
		self.n = self._validate_n(n)