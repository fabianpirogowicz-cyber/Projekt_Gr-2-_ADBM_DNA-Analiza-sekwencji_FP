import pandas as pd
import os


def export_to_csv(results, filename="output/results.csv"):
    """Eksportuje wyniki do CSV – obsługuje pojedynczy słownik lub listę słowników."""

    # Jeśli przekazano pojedynczy słownik, zamień go w listę
    if isinstance(results, dict):
        results = [results]

    if not results:
        print("Brak danych do eksportu.")
        return

    # Upewnij się, że folder istnieje
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    # Przygotowanie danych do DataFrame
    data = []
    for r in results:
        data.append({
            "motif": r["motif"],
            "count": r["count"],
            "positions": ",".join(map(str, r["positions"]))
        })

    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"Wyniki zapisano do pliku: {filename}")