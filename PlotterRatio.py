import matplotlib.pyplot as plt
import csv
import numpy as np
from scipy.optimize import curve_fit

# Definiamo la funzione logaritmica teorica di riferimento da fittare: T(n) = c * log2(n)
def log_theory(x, c):
    return c * np.log2(x)

class StandardPlotter:
    def __init__(self, filename="esperimenti_risultati/esperimenti_risultati.csv"):
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
        plt.figure(figsize=(12, 7))

        color_map = {
            "AVL": "orange",
            "RBT": "red",
            "BST": "blue",
        }

        for tree_name, data in self.results.items():
            if len(data["X"]) > 0:
                # Conversione in array numpy
                x_data = np.array(data["X"])
                y_data = np.array(data["Y"])
                
                # 1. Plot dei dati reali misurati (i punti discreti con linea continua)
                plt.plot(
                    x_data, 
                    y_data, 
                    marker='o', 
                    markersize=4,
                    linestyle='-', 
                    linewidth=1,
                    label=f"{tree_name}",
                    color=color_map[tree_name]
                )
                
                # 2. CALCOLO DELLA CURVA TEORICA (FITTING)
                # Calcola il coefficiente 'c' ottimale che minimizza lo scarto tra la teoria e i tuoi dati
                popt, _ = curve_fit(log_theory, x_data, y_data)
                c_ottimale = popt[0]
                
                # Genera un range denso di punti per disegnare una curva logaritmica
                x_smooth = np.linspace(x_data.min(), x_data.max(), 500)
                y_theory = log_theory(x_smooth, c_ottimale)
                
                # 3. Plot della curva logaritmica teorica corrispondente (linea tratteggiata)
                plt.plot(
                    x_smooth, 
                    y_theory, 
                    linestyle='--', 
                    linewidth=2.5,
                    alpha=0.8,
                    color=color_map[tree_name]
                )

        plt.title('Tempo mediano di inserimento', fontsize=14)
        plt.xlabel('Dimensione dell\'albero (N)', fontsize=12)
        plt.ylabel('Tempo Mediano (secondi)', fontsize=12)
        
        plt.grid(True, which="major", ls="--", alpha=0.5)
        plt.legend(fontsize=11, loc="upper left")
        plt.tight_layout()
        
        plt.savefig("grafico_curve_logaritmiche.png", dpi=300)
        print("=> Grafico con curve logaritmiche teoriche generato correttamente!")
        plt.show()

if __name__ == "__main__":
    plotter = StandardPlotter("esperimenti_risultati/esperimenti_risultati.csv")
    plotter.plot_time_complexity()