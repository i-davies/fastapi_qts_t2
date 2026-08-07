def calcular_status_pedido(valor_total: float, pago: bool) -> str:
    if valor_total <= 0:
        return 'invalido'
    if not pago:
        return 'pendente'
    return "confirmado"