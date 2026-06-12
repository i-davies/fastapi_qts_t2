from app.atendimento.pontuacao import (
    calcular_pontuacao_atendimento,
    classificar_atendimento,
)


def test_retorna_zero_para_tempo_invalido_zero():
    assert calcular_pontuacao_atendimento(0, True, False) == 0

def test_retorna_zero_para_tempo_invalido_negativo():
    assert calcular_pontuacao_atendimento(-3, False, True) == 0

def test_resolvido_ate_10_sem_reincidencia():
    assert calcular_pontuacao_atendimento(10, True, False) == 10

def test_resolvido_entre_11_e_20_sem_reincidencia():
    assert calcular_pontuacao_atendimento(11, True, False) == 8

def test_resolvido_limite_20_sem_reincidencia():
    assert calcular_pontuacao_atendimento(20, True, False) == 8

def test_resolvido_acima_20_com_reincidencia():
    assert calcular_pontuacao_atendimento(21, True, True) == 4

def test_nao_resolvido_ate_10_sem_reincidencia():
    assert calcular_pontuacao_atendimento(10, False, False) == 5

def test_nao_resolvido_entre_11_e_20_com_reincidencia():
    assert calcular_pontuacao_atendimento(15, False, True) == 1

def test_nao_resolvido_limite_20_sem_reincidencia():
    assert calcular_pontuacao_atendimento(20, False, False) == 3

def test_nao_resolvido_acima_20_com_reincidencia_minimo_zero():
    assert calcular_pontuacao_atendimento(25, False, True) == 0

def test_classificacao_excelente():
    assert classificar_atendimento(10) == "Excelente"


def test_classificacao_bom():
    assert classificar_atendimento(8) == "Bom"


def test_classificacao_regular():
    assert classificar_atendimento(5) == "Regular"


def test_classificacao_critico():
    assert classificar_atendimento(2) == "Crítico"


def test_fluxo_completo_resultado_excelente():
    pontuacao = calcular_pontuacao_atendimento(10, True, False)
    resultado = classificar_atendimento(pontuacao)
    assert resultado == "Excelente"


def test_fluxo_completo_resultado_bom():
    pontuacao = calcular_pontuacao_atendimento(11, True, False)
    resultado = classificar_atendimento(pontuacao)
    assert resultado == "Bom"

def test_fluxo_completo_resultado_regular():
    pontuacao = calcular_pontuacao_atendimento(10, False, False)
    resultado = classificar_atendimento(pontuacao)
    assert resultado == "Regular"

def test_fluxo_completo_resultado_critico():
    pontuacao = calcular_pontuacao_atendimento(25, False, True)
    resultado = classificar_atendimento(pontuacao)
    assert resultado == "Crítico"
