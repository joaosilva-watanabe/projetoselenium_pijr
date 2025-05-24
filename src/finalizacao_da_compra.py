from seleniumbase import BaseCase

class FinalizarCompra(BaseCase):
    def concluir_compra(self):
        # Espera para que as informações de compra estejam disponíveis
        self.wait_for_element(".summary_info_label")

        # Buscando as informações da compra
        detalhes_compra = self.find_elements(".summary_info_label")
        valor_total = self.get_text(".summary_total_label")
        detalhes_da_compra = self.find_elements(".summary_value_label")
        meio_de_pagamento = detalhes_da_compra[0].text
        forma_de_entrega = detalhes_da_compra[1].text

        #Clicando no botão para finalizar a compra
        self.click("#finish")

        # Espera a mensagem de confirmação aparecer
        self.wait_for_element(".complete-header")

        #Capturando a mensagem de confirmação
        msg_confirmacao = self.get_text(".complete-text")

        #Retornando as informações desejadas
        return print(f"\nMensagem de confirmação: '{msg_confirmacao}'\n"
                     f"Valor total: '{valor_total}'\n"
                     f"Meio de pagamento: '{meio_de_pagamento}'\n"
                     f"Forma de entrega: '{forma_de_entrega}'")
