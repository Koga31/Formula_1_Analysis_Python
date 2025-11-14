import pandas as pd
import os
import pickle
from src.utils.config import DATA_RAW, DATA_PROCESSED


def build_dataset():
    rows = []

    for file in os.listdir(DATA_RAW):
        if not file.endswith(".pkl"):
            continue

        year, _, round_n = file.replace(".pkl", "").split("_")
        year = int(year)
        rnd = int(round_n)

        ##Carrega o arquivo e acessa as informações finais da corrida.
        session = pickle.load(open(os.path.join(DATA_RAW, file), "rb"))

        results = session.results
        ##carrega os resultados da corrida por piloto
        for _, r in results.iterrows():
            rows.append({
                "year": year,
                "round": rnd,
                "driver": r["Driver"],
                "team": r["Team"],
                "grid": r["GridPosition"],
                "finish": r["Position"],
                "status": r["Status"]
            })

    df = pd.DataFrame(rows)
    df.to_csv(os.path.join(DATA_PROCESSED, "race_results.csv"), index=False)

    return df