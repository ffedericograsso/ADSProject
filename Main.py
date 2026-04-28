from ExperimentSetup import ExperimentSetup
from ExperimentRunner import ExperimentRunner

def main():
    print("Inizializzazione del setup degli esperimenti...")
    setup = ExperimentSetup(min_n=1000, max_n=10000000, steps=100)
    
    print("Avvio dell'esperimento...")
    runner = ExperimentRunner(setup, n_exp=10)
    runner.run_experiments()
    
    print("Esperimenti completati! Risultati:\n (TBD)")
    risultati = runner.get_results()

    for tree_name, data in risultati.items():
        print(f"\n{tree_name}:")
        print(f"  Valori (N):\t{data['X']}")
        print(f"  Tempi ({len(data['Y'])}):\t{[f'{t:.7f}' for t in data['Y']]}")

if __name__ == "__main__":
    main()