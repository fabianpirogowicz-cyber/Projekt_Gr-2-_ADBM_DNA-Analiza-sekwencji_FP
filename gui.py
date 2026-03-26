import tkinter as tk
from tkinter import filedialog
from dna_utils import read_fasta, analyze_motif
from visualization import plot_motif_distribution
from main import export_to_csv

def run_analysis():
    file_path = filedialog.askopenfilename()
    motif = motif_entry.get()

    sequence = read_fasta(file_path)
    result = analyze_motif(sequence, motif)

    output_label.config(
        text=f"Znaleziono {result['count']} wystąpień"
    )

    plot_motif_distribution(len(sequence), result["positions"])
    export_to_csv(result)


app = tk.Tk()
app.title("DNA Motif Analyzer")

tk.Label(app, text="Motyw DNA:").pack()
motif_entry = tk.Entry(app)
motif_entry.pack()

tk.Button(app, text="Wybierz plik i analizuj", command=run_analysis).pack()

output_label = tk.Label(app, text="")
output_label.pack()

app.mainloop()