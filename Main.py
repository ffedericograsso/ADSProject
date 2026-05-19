from ExperimentSetup import ExperimentSetup
from ExperimentRunner import ExperimentRunner
from Plotter import ResultPlotter

def main():
    print("Inizializzazione del setup degli esperimenti...")
    setup = ExperimentSetup(min_n=1000, max_n=10000000, steps=100)
    
    print("Avvio dell'esperimento...")
    runner = ExperimentRunner(setup, n_exp=10)
    runner.run_experiments()
    
    print("Esperimenti completati! Risultati:\n")
    csv_file = "esperimenti_risultati.csv"
    runner.export_to_csv(csv_file)

    print("Plot del grafico:\n")
    plotter = ResultPlotter(csv_file)
    plotter.plot_time_complexity()

if __name__ == "__main__":
    main()