import numpy as np


def calculate_motif_stats(sequence_length, positions):
    """Oblicza statystyki dla pozycji motywów."""
    if not positions:
        return {
            "count": 0, "density": 0.0, "mean_position": 0, "median_position": 0,
            "std_position": 0, "min_position": 0, "max_position": 0, "intervals": []
        }

    positions = np.array(positions)
    count = len(positions)
    density = count / sequence_length * 100

    stats = {
        "count": count,
        "density": round(density, 2),
        "mean_position": int(np.mean(positions)),
        "median_position": int(np.median(positions)),
        "std_position": round(np.std(positions), 2),
        "min_position": int(np.min(positions)),
        "max_position": int(np.max(positions)),
        "positions": positions.tolist()
    }

    if count > 1:
        intervals = np.diff(positions).tolist()
        stats["intervals"] = intervals
        stats["mean_interval"] = int(np.mean(intervals))

    return stats


def print_stats(stats, motif_name):
    """Wyświetla statystyki w czytelnej formie."""
    print(f"\n📊 STATYSTYKI dla motywu '{motif_name}'")
    print(f"  Liczba wystąpień: {stats['count']}")
    print(f"  Gęstość: {stats['density']}%")
    print(f"  Średnia pozycja: {stats['mean_position']}")
    print(f"  Mediana pozycji: {stats['median_position']}")
    print(f"  Odchylenie std: {stats['std_position']}")
    print(f"  Zakres pozycji: {stats['min_position']}-{stats['max_position']}")

    if 'mean_interval' in stats:
        print(f"  Średni odstęp: {stats['mean_interval']} bp")