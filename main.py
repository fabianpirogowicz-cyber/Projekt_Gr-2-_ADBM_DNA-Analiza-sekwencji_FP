from dna_utils import read_fasta, analyze_motif
from visualization import plot_motif_distribution
from export import export_to_csv
from statistics import calculate_motif_stats, print_stats  # ✅ Nowe importy


def main():
    file_path = "data/example.fasta"
    motifs = ["ATG", "TATA", "CGCG"]

    sequence = read_fasta(file_path)
    seq_length = len(sequence)

    all_results = []

    for motif in motifs:
        result = analyze_motif(sequence, motif)
        result["motif"] = motif

        # ✅ OBLICZENIA STATYSTYCZNE
        stats = calculate_motif_stats(seq_length, result["positions"])
        result.update(stats)  # Dodaj statystyki do wyniku

        all_results.append(result)

        # ✅ Wyświetl statystyki
        print_stats(stats, motif)

        print("-" * 50)

        # Wykres dla każdego motywu
        plot_motif_distribution(
            seq_length,
            result["positions"],
            output_file=f"output/motif_{motif}.png"
        )

    # Eksport wszystkich wyników (z nowymi statystykami) do CSV
    export_to_csv(all_results, "output/motif_results.csv")
    print("\n✅ Pełna analiza ze statystykami zakończona!")


if __name__ == "__main__":
    main()