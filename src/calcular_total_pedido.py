"""Cálculo do valor final de um pedido de e-commerce."""

from math import isfinite


DESCONTOS_FIDELIDADE = {
    "REGULAR": 0.0,
    "VIP": 0.05,
    "PREMIUM": 0.10,
}

FRETE_BASE = 15.00
CUSTO_POR_QUILO = 5.00


def calcular_total_pedido(
    valor_bruto: float,
    categoria_cliente: str,
    cupons: list[str],
    peso_kg: float,
) -> float:
    """Calcula o total do pedido após descontos e frete."""
    if not isfinite(valor_bruto):
        raise ValueError("O valor bruto do pedido deve ser um número finito.")
    if valor_bruto <= 0:
        raise ValueError("O valor bruto do pedido deve ser maior que zero.")
    if not isfinite(peso_kg):
        raise ValueError("O peso do pacote deve ser um número finito.")
    if peso_kg < 0:
        raise ValueError("O peso do pacote não pode ser negativo.")
    if categoria_cliente not in DESCONTOS_FIDELIDADE:
        raise ValueError("Categoria de cliente inválida.")

    total_produtos = valor_bruto * (1 - DESCONTOS_FIDELIDADE[categoria_cliente])
    if "DESC10" in cupons:
        total_produtos *= 0.90

    frete = FRETE_BASE + (peso_kg * CUSTO_POR_QUILO)
    if "FRETE_GRATIS" in cupons:
        frete = 0.0

    return round(total_produtos + frete, 2)
