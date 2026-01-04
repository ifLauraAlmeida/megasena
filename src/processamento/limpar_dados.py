import pandas as pd

def processar_dados(data: dict) -> pd.DataFrame:
    data["dezenas_sorteadas"] = [
        int(num) for num in data["dezenasSorteadasOrdemSorteio"]
    ]

    df = pd.DataFrame([data])

    df = df[[
        "dataApuracao",
        "dezenas_sorteadas",
        "valorArrecadado",
        "numero",
    ]]

    df = df.rename(columns={
        "dataApuracao": "data_apuracao",
        "valorArrecadado": "valor_arrecadado",
        "numero": "numero_concurso",
    })

    return df
