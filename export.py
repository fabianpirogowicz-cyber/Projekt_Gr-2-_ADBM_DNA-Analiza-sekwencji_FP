import pandas as pd

def export_to_csv(results, filename="output/results.csv"):
    df = pd.DataFrame({
        "motif": [results["motif"]],
        "count": [results["count"]],
        "positions": [",".join(map(str, results["positions"]))]
    })
    df.to_csv(filename, index=False)