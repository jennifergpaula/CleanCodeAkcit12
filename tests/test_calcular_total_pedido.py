import unittest
from math import inf, nan

from src.calcular_total_pedido import calcular_total_pedido


class CalcularTotalPedidoTests(unittest.TestCase):
    def test_aplica_desconto_vip_cupom_e_frete(self):
        total = calcular_total_pedido(200.00, "VIP", ["DESC10"], 2.0)

        self.assertEqual(total, 196.00)

    def test_frete_gratis_para_pedido_regular_sem_peso(self):
        total = calcular_total_pedido(100.00, "REGULAR", ["FRETE_GRATIS"], 0.0)

        self.assertEqual(total, 100.00)

    def test_rejeita_valor_bruto_negativo(self):
        with self.assertRaisesRegex(
            ValueError, "O valor bruto do pedido deve ser maior que zero."
        ):
            calcular_total_pedido(-50.00, "VIP", [], 1.0)

    def test_rejeita_valor_bruto_nao_finito(self):
        for valor_bruto in (nan, inf, -inf):
            with self.subTest(valor_bruto=valor_bruto):
                with self.assertRaisesRegex(
                    ValueError, "O valor bruto do pedido deve ser um número finito."
                ):
                    calcular_total_pedido(valor_bruto, "VIP", [], 1.0)

    def test_rejeita_peso_negativo(self):
        with self.assertRaisesRegex(
            ValueError, "O peso do pacote não pode ser negativo."
        ):
            calcular_total_pedido(50.00, "VIP", [], -1.0)

    def test_rejeita_peso_nao_finito(self):
        for peso_kg in (nan, inf, -inf):
            with self.subTest(peso_kg=peso_kg):
                with self.assertRaisesRegex(
                    ValueError, "O peso do pacote deve ser um número finito."
                ):
                    calcular_total_pedido(50.00, "VIP", [], peso_kg)

    def test_rejeita_categoria_invalida(self):
        with self.assertRaisesRegex(ValueError, "Categoria de cliente inválida."):
            calcular_total_pedido(50.00, "INVALIDA", [], 1.0)

    def test_ignora_cupons_invalidos_e_duplicados(self):
        total = calcular_total_pedido(
            100.00, "REGULAR", ["DESC10", "DESC10", "CUPOM_INVALIDO"], 0.0
        )

        self.assertEqual(total, 105.00)


if __name__ == "__main__":
    unittest.main()
