import matplotlib.pyplot as plt
import time
import sys
import numpy as np
from scipy.optimize import curve_fit

# Assicuriamo l'inclusione dei moduli della cartella principale
sys.path.append(".")
from Project import Project

# Modello lineare per il BST nel caso peggiore: T(n) = c * n
def linear_theory(x, c):
    return c * x

# Modello logaritmico per AVL e RBT: T(n) = c * log2(n)
def log_theory(x, c):
    return c * np.log2(x)

def run_real_worst_case():
    # Valori di N controllati per mostrare la crescita lineare del BST senza piantare la CPU
    N_values = [100, 500, 1000, 2500, 5000, 7500, 10000]
    
    structures = ["BST", "AVL", "RBT"]
    results = {struct: [] for struct in structures}
    
    print("Avvio benchmark del CASO PESSIMO VERO (Input ordinato sequenzialmente)...")
    
    for struct_name in structures:
        print(f"Esecuzione su struttura: {struct_name}...")
        for n in N_values:
            # Creazione di elementi già perfettamente ordinati crescenti
            ordered_keys = list(range(n))
            
            # Istanziamo la struttura tramite la Factory del vostro progetto
            project = Project(struct_name, n)
            tree = project.tree
            
            # Popoliamo l'albero in modo silenzioso fino a n-1 elementi
            for i in range(n - 1):
                node = project.create_node(ordered_keys[i])
                tree.insert(node)
                
            # Misuriamo millimetricamente l'inserimento dell'ennesimo elemento degenere
            target_key = ordered_keys[-1]
            target_node = project.create_node(target_key)
            
            start_time = time.perf_counter()
            tree.insert(target_node)
            end_time = time.perf_counter()
            
            results[struct_name].append(end_time - start_time)
            
    # --- Generazione del Grafico del Caso Pessimo con Regressioni ---
    plt.figure(figsize=(11, 6.5))
    color_map = {"BST": "blue", "AVL": "orange", "RBT": "red"}
    
    for struct_name in structures:
        x_data = np.array(N_values)
        y_data = np.array(results[struct_name])
        
        # 1. Plottiamo i dati sperimentali reali
        plt.plot(
            x_data, 
            y_data, 
            marker='x', 
            linestyle='-', 
            linewidth=1.2,
            label=f"{struct_name}", 
            color=color_map[struct_name]
        )
        
        # 2. Calcolo e fitting della regressione in base al modello teorico corretto
        x_smooth = np.linspace(x_data.min(), x_data.max(), 500)
        
        if struct_name == "BST":
            # Il BST degenera in lista -> fitting lineare O(N)
            popt, _ = curve_fit(linear_theory, x_data, y_data)
            y_theory = linear_theory(x_smooth, popt[0])
        else:
            # AVL e RBT rimangono bilanciati -> fitting logaritmico O(log N)
            popt, _ = curve_fit(log_theory, x_data, y_data)
            y_theory = log_theory(x_smooth, popt[0])
            
        # 3. Plottiamo la linea di regressione teorica corrispondente
        plt.plot(
            x_smooth, 
            y_theory, 
            linestyle='--', 
            linewidth=2, 
            alpha=0.75,
            color=color_map[struct_name]
        )
                 
    plt.title('Tempo di inserimento con sequenza pre-ordinata', fontsize=14)
    plt.xlabel('Dimensione dell\'albero (N)', fontsize=12)
    plt.ylabel('Tempo di Inserimento (secondi)', fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend(fontsize=10, loc="upper left")
    plt.tight_layout()
    
    # Salvataggio dell'immagine per la relazione LaTeX
    plt.savefig("grafico_caso_pessimo.png", dpi=300)
    print("\n=> Grafico del caso pessimo con regressioni salvato come 'grafico_caso_pessimo_reale.png'!")
    plt.show()

if __name__ == "__main__":
    run_real_worst_case()