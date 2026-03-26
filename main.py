from dna_utils import read_fasta, analyze_motif
from visualization import plot_motif_distribution
from export import export_to_csv

def main():
    file_path = "data/example.fasta"
    motif = "ATG"

    sequence = read_fasta(file_path)
    result = analyze_motif(sequence, motif)

    print(result)

    plot_motif_distribution(len(sequence), result["positions"])
    export_to_csv(result)


if __name__ == "__main__":
    main()