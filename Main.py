from ExperimentSetup import ExperimentSetup
from ExperimentRunner import ExperimentRunner
from PlotterMain import ResultPlotter

def main():
    print("Inizializzazione del setup degli esperimenti...")
    setup = ExperimentSetup(min_n=1000, max_n=10000000, steps=100)
    
    runner = ExperimentRunner(setup, n_exp=10)
    runner.run_experiments()

    nome_file = "esperimenti_risultati.csv"
    runner.export_to_csv(nome_file)

    plotter = ResultPlotter(nome_file)
    plotter.plot_time_complexity()

if __name__ == "__main__":
    main()