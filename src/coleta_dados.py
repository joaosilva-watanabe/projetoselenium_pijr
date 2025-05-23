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
        #Percorre a lista de produtos
        for produto in produtos:
            nome = produto.find_element("css selector", ".inventory_item_name").text
            descrição = produto.find_element("css selector", ".inventory_item_desc").text
            preço = produto.find_element("css selector", ".inventory_item_price").text
            #Adiciona os dados na lista
            nomes.append(nome)
            descrições.append(descrição)
            preços.append(preço)
        
