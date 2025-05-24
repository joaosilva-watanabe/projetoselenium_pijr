from login import LoginSauceDemo
from adicionar_ao_carrinho import AdicionarAoCarrinho
from checkout import Checkout
from finalizacao_da_compra import FinalizarCompra
from coleta_dados import ColetarDados

#Rodando um teste do script com todas as funções criadas>
class TestExecutarCompra(LoginSauceDemo, ColetarDados, AdicionarAoCarrinho, Checkout, FinalizarCompra):
    def test_fluxo_completo_de_compra(self):
        self.login()
        self.coleta_dados()
        self.adicionar_produtos()
        self.preencher_formulario_checkout()
        self.concluir_compra()
