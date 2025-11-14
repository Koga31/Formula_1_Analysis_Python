import os

##BASE_DIR: calcula a pasta raiz do projeto automaticamente.
## isso auxilia o código a funciona em qualquer máquina (*IMPORTANTE)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DATA_RAW = os.path.join(BASE_DIR, "data", "raw")
DATA_PROCESSED = os.path.join(BASE_DIR, "data", "processed")
FASTF1_CACHE = os.path.join(BASE_DIR, "data", "cache")