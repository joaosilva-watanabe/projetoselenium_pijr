from seleniumbase import BaseCase

class FinalizarCompra(BaseCase):
    def concluir_compra(self):
        valor_total = self.get_text(".summary_total_label")

        # Buscando as informações da compra
        detalhes_da_compra = self.find_elements(".summary_value_label")
        meio_de_pagamento = detalhes_da_compra[0].text
        forma_de_entrega = detalhes_da_compra[1].text

        #Clicando no botão para finalizar a compra
        self.click("#finish")

        #Capturando a mensagem de confirmação
        msg_confirmacao = self.get_text(".complete-text")

        #Retornando as informações desejadas
        return print(f"\nMensagem de confirmação: '{msg_confirmacao}'\n"
                     f"Valor total: '{valor_total}'\n"
                     f"Meio de pagamento: '{meio_de_pagamento}'\n"
                     f"Forma de entrega: '{forma_de_entrega}'")
