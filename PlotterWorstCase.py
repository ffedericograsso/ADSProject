import matplotlib.pyplot as plt
import time
import sys

# Assicuriamo l'inclusione dei moduli della cartella principale
sys.path.append(".")
from Project import Project

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
            
    # --- Generazione del Grafico del Caso Pessimo ---
    plt.figure(figsize=(10, 6))
    color_map = {"BST": "blue", "AVL": "orange", "RBT": "red"}
    
    for struct_name in structures:
        plt.plot(
            N_values, 
            results[struct_name], 
            marker='x', 
            linestyle='-', 
            label=f"{struct_name} (Input Ordinato)", 
            color=color_map[struct_name]
        )
                 
    plt.title('Caso Pessimo: Tempo di inserimento con sequenza pre-ordinata', fontsize=14)
    plt.xlabel('Dimensione dell\'albero (N)', fontsize=12)
    plt.ylabel('Tempo di Inserimento (secondi)', fontsize=12)
    plt.grid(True, which="both", ls="--", alpha=0.5)
    plt.legend(fontsize=12)
    plt.tight_layout()
    
    # Salvataggio dell'immagine per la relazione LaTeX
    plt.savefig("grafico_caso_pessimo_reale.png", dpi=300)
    print("\n=> Grafico del caso pessimo salvato come 'grafico_caso_pessimo_reale.png'!")
    plt.show()

if __name__ == "__main__":
    run_real_worst_case()