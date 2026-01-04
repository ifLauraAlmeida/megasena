import pandas as pd
from .comparar_aposta import comparar_aposta

df = pd.read_csv(
    "data/processed/megasena.csv",
    parse_dates=["data_apuracao"]
)

print("🎰 Mega-Sena — Simulador Histórico")

while True:
    entrada = input("\nDigite 6 números separados por espaço: ").strip()

    try:
        aposta = sorted(map(int, entrada.split()))

        if len(aposta) != 6 or any(n < 1 or n > 60 for n in aposta):
            raise ValueError

    except ValueError:
        print("❌ Entrada inválida. Use 6 números entre 1 e 60.")
        continue

    resultados = comparar_aposta(df, aposta)

    if resultados:
        for r in resultados:
            print(
                f"🎯 {r['acertos']} acertos | "
                f"Concurso {r['concurso']} | "
                f"Ano {r['ano']}"
            )
    else:
        print("💀 Nunca pontuou (nem quadra).")

    if input("\nQuer apostar novamente? (s/n): ").lower() != "s":
        break
