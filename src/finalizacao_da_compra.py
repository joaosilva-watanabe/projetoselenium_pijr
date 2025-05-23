from seleniumbase import BaseCase

class FinalizarCompra(BaseCase):
    def concluir_compra(self):

        meio_de_pagamento = self.get_text(".summary_value_label", timeout= None)
        forma_de_entrega = self.get_text("", timeout= None)
        valor_total = self.get_text(".summary_total_label")
        self.click("#finish")
        msg_confirmacao = self.get_text(".complete-text")

        return print(f"Mensagem de confirmação: '{msg_confirmacao}'\n "
                     f"Valor total: '{valor_total}'\n"
                     f"Meio de pagamento: '{meio_de_pagamento}'\n"
                     f"Forma de entrega: '{forma_de_entrega}'")
