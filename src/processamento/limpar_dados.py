import pandas as pd

def processar_dados(data: dict) -> pd.DataFrame:
    data["dezenas_sorteadas"] = [
        int(num) for num in data["dezenasSorteadasOrdemSorteio"]
    ]

    df = pd.DataFrame([data])

    df = df[[
        "dataApuracao",
        "dezenas_sorteadas",
        "numero",
    ]]

    df = df.rename(columns={
        "dataApuracao": "data_apuracao",
        "numero": "numero_concurso",
    })

    return df

