from seleniumbase import BaseCase

class ColetarDados(BaseCase):
    #Cria função
    def coleta_dados(self):
        #Abrir a página no navegador
        self.open("https://www.saucedemo.com/")
        #Espera o carregamento da página
        self.wait_for_element(".inventory_list")
        #Cria listas para armazenar os dados
        nomes = []
        descrições = []
        preços = []
        #Acha os produtos
        produtos = self.find_elements(".inventory_item")
