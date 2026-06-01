import matplotlib.pyplot as plt
import csv

class StandardPlotter:
    def __init__(self, filename="esperimenti_risultati/esperimenti_risultati_Mac1.csv"):
        self.filename = filename
        self.results = {
            "AVL": {"X": [], "Y": []},
            "RBT": {"X": [], "Y": []},
            "BST": {"X": [], "Y": []},
            
        }
        self._load_from_csv()

    def _load_from_csv(self):
        with open(self.filename, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                tree_name = row["Tree"]
                n = float(row["N"])
                median_time = float(row["Mediana tempo (s)"])
                
                if tree_name in self.results:
                    self.results[tree_name]["X"].append(n)
                    self.results[tree_name]["Y"].append(median_time)

    def plot_time_complexity(self):
        plt.figure(figsize=(10, 6))

        color_map = {
            "AVL": "orange",
            "RBT": "red",
            "BST": "blue",
            
        }

        for tree_name, data in self.results.items():
            if len(data["X"]) > 0:
                plt.plot(
                    data["X"], 
                    data["Y"], 
                    marker='o', 
                    markersize=4,
                    linestyle='-', 
                    label=tree_name,
                    color=color_map[tree_name]
                )

        plt.title('Tempo mediano di inserimento su alberi di dimensione N', fontsize=14)
        plt.xlabel('Dimensione dell\'albero (N)', fontsize=12)
        plt.ylabel('Tempo Mediano (secondi)', fontsize=12)
        
        plt.grid(True, which="major", ls="--", alpha=0.5)
        plt.legend(fontsize=12)
        plt.tight_layout()
        
        plt.savefig("grafico_curve_logaritmiche.png", dpi=300)
        print("=> Grafico generato correttamente!")
        plt.show()

if __name__ == "__main__":
    # Assicurati che il nome del file CSV sia quello corretto generato dai tuoi test
    plotter = StandardPlotter("esperimenti_risultati/esperimenti_risultati.csv")
    plotter.plot_time_complexity()