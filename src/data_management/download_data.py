import fastf1
from fastf1 import plotting
from tqdm import tqdm
import os
from src.utils.config import FASTF1_CACHE, DATA_RAW

##Ativa o cache para não baixar os mesmos dados de novo. (torna o algoritmo mais rápido)
fastf1.Cache.enable_cache(FASTF1_CACHE)

def download_season(year: int):
    for rnd in tqdm(range(1, 25), desc=f"Downloading data from {year}"):
        ##Tenta baixar todos os rounds das corridas (nem todos existem)
        try:
            session = fastf1.get_session(year, rnd, "R") ##'R' = Race
            session.load()
            session.save(os.path.join(DATA_RAW, f"{year}_round_{rnd}.pkl")) ##Salva a sessão inteira como pickle -> não precisamos baixar denovo
        except Exception:
            continue

if __name__ == "__main__":
    years = range(2018, 2025)
    for y in years:
        download_season(y)