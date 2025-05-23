from seleniumbase import BaseCase

class AdicionarAoCarrinho(BaseCase):
    def adicionar_produtos(self):
        produtos = self.find_elements(".btn_inventory")
        total_de_produtos = 0
        for produto in produtos:
            produto.click()
            total_de_produtos += 1
        self.click("#shopping_cart_container")
