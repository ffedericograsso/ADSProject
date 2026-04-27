import math
from KeyManager import KeyManager
from Project import Project

# Setup dell'esperimento
class ExperimentSetup:
	def __init__(self, min_n=1000, max_n=10000000, steps=100):
		self.min_n = min_n
		self.max_n = max_n
		self.steps = steps
		self.n_values = self._calculate_n_progr()

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
	def experiment_tree_setup(self, project: Project):
		tree = project.tree

		key_manager = KeyManager(project.n)

		# Popolazione iniziale
		for _ in range(project.n):
			random_key = key_manager.get_key_insert()
			node_to_insert = project.create_node(random_key)
			tree.insert(random_key)

		# Ora:
		# - L'albero ha n nodi
		# - Il KeyManager ha indice m pari a n
		# - Esiste esattamente una chiave in key_manager.A[n] disponibile per i test successivi

		return tree, key_manager