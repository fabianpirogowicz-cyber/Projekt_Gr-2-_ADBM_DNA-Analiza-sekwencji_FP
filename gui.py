import tkinter as tk
from tkinter import filedialog
from dna_utils import read_fasta, analyze_motif
from visualization import plot_motif_distribution
from export import export_to_csv  # ✅ Import bezpośrednio z modułu export


def run_analysis():
    file_path = filedialog.askopenfilename()
    motif = motif_entry.get()

    if not file_path or not motif:
        output_label.config(text="Wybierz plik i podaj motyw!")
        return

    sequence = read_fasta(file_path)
    result = analyze_motif(sequence, motif)

    output_label.config(
        text=f"Znaleziono {result['count']} wystąpień"
    )

    # Zapisz wykres do pliku, aby uniknąć problemów z GUI w Tkinter
    plot_file = f"output/motif_{motif}.png"
    plot_motif_distribution(len(sequence), result["positions"], output_file=plot_file)

    # Eksport do CSV (funkcja obsługuje teraz pojedynczy słownik dzięki isinstance)
    export_to_csv(result)


app = tk.Tk()
app.title("DNA Motif Analyzer")

tk.Label(app, text="Motyw DNA:").pack()
motif_entry = tk.Entry(app)
motif_entry.pack()

tk.Button(app, text="Wybierz plik i analizuj", command=run_analysis).pack()

output_label = tk.Label(app, text="")
output_label.pack()

# Upewnij się, że folder output istnieje (opcjonalne, ale zalecane)
import os

os.makedirs("output", exist_ok=True)

app.mainloop()