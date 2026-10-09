import time

import pytest

from app.faturamento.cobranca import processar_cobranca


@pytest.mark.parametrize(
    "valor_base, plano, dias_atraso, retorno_esperado",
    [
        # Entradas inválidas
        (0.0, "BRONZE", 0, -1.0),
        (-50.0, "PRATA", 0, -1.0),
        (100.0, "BRONZE", -1, -1.0),
        (100.0, "VIP", 0, -2.0),
        (100.0, "", 0, -2.0),
        # Pagamento em dia (dias_atraso == 0)
        (100.0, "BRONZE", 0, 100.0),
        (100.0, "PRATA", 0, 85.0),
        (100.0, "OURO", 0, 75.0),
        # Normalização de texto
        (100.0, "  prata  ", 0, 85.0),
        # Atraso moderado (1 a 20 dias) e valores de fronteira
        (100.0, "BRONZE", 1, 108.4),
        (100.0, "PRATA", 10, 96.4),
        (100.0, "BRONZE", 20, 116.0),
        # Atraso severo (> 20 dias) e valores de fronteira
        (100.0, "BRONZE", 21, 146.8),
        (100.0, "OURO", 30, 123.0),
    ],
)
def test_processar_cobranca_funcional(
    valor_base, plano, dias_atraso, retorno_esperado
):
    """Valida a corretude de todas as regras funcionais e valores de fronteira."""
    assert (
        processar_cobranca(valor_base, plano, dias_atraso) == retorno_esperado
    )


def test_tempo_processamento_cobranca_nao_funcional():
    """Valida o requisito operacional não funcional de tempo de resposta."""
    inicio = time.perf_counter()
    resultado = processar_cobranca(100.0, "BRONZE", 0)
    fim = time.perf_counter()
    tempo_decorrido = fim - inicio

    assert resultado == 100.0
    # O tempo deve ser estritamente inferior a 80 milissegundos (0.08 segundos)
    assert tempo_decorrido < 0.08