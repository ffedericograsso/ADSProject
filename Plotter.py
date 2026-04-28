import matplotlib.pyplot as plt

class ResultPlotter:
    def __init__(self, results_data):
        self.results = results_data

    def plot_time_complexity(self):
        # Imposta la grandezza della finestra del grafico
        plt.figure(figsize=(10, 6))

        color_map = {
            "BST": "blue",
            "AVL": "orange",
            "RBT": "red"
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
        
        # Uso scala logaritmica sull'asse X per via della progressione geometrica usata 
        plt.xscale('log')
        plt.grid(True, which="both", ls="--", alpha=0.5)
        plt.legend(fontsize=12)
        
        print("\n=> Generazione grafico completata! Chiudi la finestra per terminare il programma.")
        plt.tight_layout()
        plt.show()