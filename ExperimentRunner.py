import time
from BST import BST as SimpleBST
from AVL import AVL
from RBT import RBTree
from ExperimentSetup import ExperimentSetup

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