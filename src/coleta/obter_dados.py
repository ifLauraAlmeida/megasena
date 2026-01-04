import requests

def obter_dados(numero_concurso: int) -> dict:
    url = f"https://servicebus2.caixa.gov.br/portaldeloterias/api/megasena/{numero_concurso}"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }

    resposta = requests.get(url, timeout=60, headers=headers)
    resposta.raise_for_status()

    return resposta.json()