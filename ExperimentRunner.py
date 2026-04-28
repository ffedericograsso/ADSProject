import time
import statistics
from ExperimentSetup import ExperimentSetup
from Project import Project

# Runner dell'esperimento
class ExperimentRunner:
	def __init__(self, setup_config: ExperimentSetup, n_exp=10):
		self.setup = setup_config
		self.n_exp = n_exp
		self.results = {
			"BST": {"X": [], "Y": []},
			"AVL": {"X": [], "Y": []},
			"RBT": {"X": [], "Y": []}
		}

	def run_experiments(self):
		trees_to_test = ["BST", "AVL", "RBT"]

		# Iterazione su tutti i valori di N del setup
		for j, n in enumerate(self.setup.n_values):
			print(f"ESPERIMENTO {j+1}/{len(self.setup.n_values)} - Dimensione N = {n}...")

			for tree_name in trees_to_test:
				print(f" [{tree_name}]")
				project = Project(tree_name, n)

				# 1. SETUP da Experiment Setup
				tree, key_manager = self.setup.experiment_tree_setup(project)

				partial_insert_times = []

				# 2. MISURAZIONE insert(available_key)
				# Dato che m = n, la chiave da inserire è A[n]
				for i in range(self.n_exp):
					available_key = key_manager.get_key_insert()
					node_to_insert = project.create_node(available_key)

					start = time.perf_counter()
					tree.insert(node_to_insert)
					stop = time.perf_counter()

					duration = stop - start

					partial_insert_times.append(duration)

					print(f"		Misurazione {i+1}: Inserita chiave {available_key} in {duration:.8f} secondi")

					key_to_remove = key_manager.get_key_remove()
					node_to_remove = tree.find(key_to_remove)
					tree.remove(node_to_remove)

				median_time = statistics.median(partial_insert_times)
				print(f" -> [{tree_name}] MEDIANA DEI TEMPI per N={n}: {median_time:.8f} secondi\n")

				self.results[tree_name]["X"].append(n)
				self.results[tree_name]["Y"].append(median_time)

	def get_results(self):
		return self.results