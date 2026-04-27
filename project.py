import math
import random
import time

from BST import BST as SimpleBST, TreeNode as BSTNode
from AVL import AVL, TreeNode as AVLNode
from RBT import RBTree, TreeNode as RBTNode
from KeyManager import KeyManager


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

		raise ValueError("structure must be BST, AVL or RBT")

	# Si assicura che il valore n sia un intero strettamente positivo
	def _validate_n(self, n):
		if not isinstance(n, int) or n <= 0:
			raise ValueError("n must be a positive integer")
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


# Setup dell'esperimento
class ExperimentSetup:
	def __init__(self, min_n=1000, max_n=10000000, steps=100):
		self.min_n = min_n
		self.max_n = max_n
		self.steps = steps
		self.n_values = self._calculate_n_sequence()

	# -- Calcolo progressione geometrica -- 
	# Calcola e restituisce la lista dei valori n generati dalla progressione
	def _calculate_n_progr(self):
		n_list = []

		# Caso base
		if self.steps <= 1:
			return [self.min_n]
		
		# Calcolo della progressione geometrica
		c = (self.max_n / self.min_n) ** (1 / (self.steps - 1))

		for i in range(self.steps):
			# Calcolo n_i = min_n * (c^i)
			val = self.min_n * (c ** i)
			n_list.append(math.floor(val))

		return n_list
	
	# -- Inizializzazione Algoritmo --
	# Restituisce l'albero popolato e il KeyManager pronto con l'ultima chiave
	def experiment_tree_setup(self, tree_class, n):
		tree = tree_class()

		key_manager = KeyManager(n)

		# Popolazione iniziale
		for _ in range(n):
			random_key = key_manager.get_key_insert()
			tree.insert(random_key)

		# Ora:
		# - L'albero ha n nodi
		# - Il KeyManager ha indice m pari a n
		# - Esiste esattamente una chiave in key_manager.A[n] disponibile per i test successivi

		return tree, key_manager

# Runner dell'esperimento
class ExperimentRunner:
	def __init__(self, setup_config: ExperimentSetup):
		self.setup = setup_config

		# Salvo i risultati
		self.results = {
			"BST": [],
			"AVL": [],
			"RBT": []
		}

	def run_experiments(self):
		trees_to_test = [("BST", SimpleBST), ("AVL", AVL), ("RBT", RBTree)]

		# Iterazione su tutti i valori di N del setup
		for n in self.setup.n_values:
			print(f"Esecuzione esperimenti per N = {n}...")

			for tree_name, tree_class in trees_to_test:
				# 1. SETUP da Experiment Setup
				tree, key_manager = self.setup.experiment_tree_setup(tree_class, n)

				# 2. MISURAZIONE (PER ORA SOLO INSERIMENTO)
				# Dato che m = n, la chiave da inserire è A[n]
				available_key = key_manager.get_key_insert()

				start = time.perf_counter()

				tree.insert(available_key)

				stop = time.perf_counter()
				duration = stop - start

				self.results[tree_name].append({
					"N": n,
					"insert_time": duration
				})

	def get_results(self):
		return self.results
