import time
import pandas as pd
from tqdm import tqdm

from src.coleta.obter_dados import obter_dados
from src.processamento.limpar_dados import processar_dados
from src.utils import salvar_csv

dfs = []

for numero in tqdm(range(1, 2956)):
    try:
        dados = obter_dados(numero)
        df = processar_dados(dados)
        dfs.append(df)
        time.sleep(0.2)
    except Exception as e:
        print(f"Erro no concurso {numero}: {e}")

df_final = pd.concat(dfs, ignore_index=True)

salvar_csv(df_final, "data/processed/megasena.csv")

print("Arquivo megasena.csv gerado com sucesso!")
