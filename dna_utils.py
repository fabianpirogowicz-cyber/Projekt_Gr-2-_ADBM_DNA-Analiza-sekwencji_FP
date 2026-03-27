import pandas as pd

def read_fasta(file_path):
    sequence = ""
    with open(file_path, "r") as f:
        for line in f:
            if not line.startswith(">"):
                sequence += line.strip()
    return sequence.upper()


def find_motif(sequence, motif):
    positions = []
    motif_len = len(motif)

    for i in range(len(sequence) - motif_len + 1):
        if sequence[i:i + motif_len] == motif:
            positions.append(i)

    return positions


def analyze_motif(sequence, motif):
    positions = find_motif(sequence, motif)

    return {
        "motif": motif,
        "count": len(positions),
        "positions": positions
    }


def segment_sequence(sequence, window_size=100):
    segments = [sequence[i:i+window_size] for i in range(0, len(sequence), window_size)]
    return pd.DataFrame({
        "segment": range(len(segments)),
        "length": [len(s) for s in segments]
    })