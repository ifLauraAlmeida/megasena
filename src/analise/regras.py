def contar_acertos(aposta, sorteio):
    return len(set(aposta) & set(sorteio))