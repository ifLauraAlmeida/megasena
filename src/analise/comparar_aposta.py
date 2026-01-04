from .regras import contar_acertos
import ast
import pandas as pd

def comparar_aposta(df, aposta):
    resultados = []
    aposta_set = set(aposta)

    for _, row in df.iterrows():
        sorteio = set(ast.literal_eval(row["dezenas_sorteadas"]))
        acertos = len(aposta_set & sorteio)

        if acertos >= 4:
            data = pd.to_datetime(row["data_apuracao"], dayfirst=True, errors="coerce")

            resultados.append({
                "concurso": row["numero_concurso"],
                "ano": data.year if not pd.isna(data) else None,
                "acertos": acertos
            })

    return resultados
