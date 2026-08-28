import time

def processar_pagamento(valor: float) -> bool:
    """Simula o tempo de processamento de um gateway de pagamento"""
    if valor < 0:
        return False

    # Simula latência de rede ou comunicação com API externa
    time.sleep(0.05)
    return True