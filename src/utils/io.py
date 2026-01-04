import pandas as pd
from pathlib import Path


def carregar_csv(caminho):
    caminho = Path(caminho)
    if not caminho.exists():
        raise FileNotFoundError(f"Arquivo não encontrado: {caminho}")
    return pd.read_csv(caminho)


def salvar_csv(df, caminho):
    caminho = Path(caminho)
    caminho.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(caminho, index=False)
