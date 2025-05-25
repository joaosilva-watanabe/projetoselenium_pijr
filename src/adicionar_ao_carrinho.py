from seleniumbase import BaseCase

class AdicionarAoCarrinho(BaseCase):
    def adicionar_produtos(self):
        #Espera para que todos os botões de adicionar ao carrinho sejam carregados
        self.wait_for_element(".btn_inventory")

        #Encontrando os produtos
        produtos = self.find_elements(".btn_inventory")

        #loop para clicar nos botões para adicionar ao carrinho
        for produto in produtos:
            produto.click()

        #Clicando no botão para concluir o processo
        self.click("#shopping_cart_container")
