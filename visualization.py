import matplotlib.pyplot as plt

def plot_motif_distribution(sequence_length, positions, output_file=None):
    plt.figure(figsize=(10, 2))

    plt.scatter(positions, [1]*len(positions), marker='|')
    plt.title("Rozmieszczenie motywów w sekwencji")
    plt.xlabel("Pozycja w sekwencji")
    plt.yticks([])

    if output_file:
        plt.savefig(output_file)

    plt.show()