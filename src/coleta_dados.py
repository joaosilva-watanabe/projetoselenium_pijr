from seleniumbase import BaseCase

class ColetarDados(BaseCase):
    #Definindo a função para salvar os dados
    def salvar_csv(self, nomes, precos, descricoes):
        import csv

        with open('../data/info.csv', 'w', newline='', encoding='utf8') as arquivo:
            writer = csv.writer(arquivo)

            # Escrevendo o cabeçalho
            writer.writerow(['Nome do Produto','Preço ($)','Descrição'])

            # Escrever as informações
            for i in range(len(nomes)):
                writer.writerow([nomes[i], precos[i], descricoes[i]])
            print("Dados salvos em 'info.csv'")

    #Criando a função para coletar os dados
    def coleta_dados(self):
        #Espera o carregamento da página
        self.wait_for_element(".inventory_list")

        #Cria listas para armazenar os dados
        nomes = []
        precos = []
        descricoes = []

        #Acha os produtos
        produtos = self.find_elements(".inventory_item")

        #Percorre a lista de produtos
        for produto in produtos:
            nome = produto.find_element("css selector", ".inventory_item_name").text
            preco = produto.find_element("css selector", ".inventory_item_price").text
            descricao = produto.find_element("css selector", ".inventory_item_desc").text

            #Adiciona os dados na lista
            nomes.append(nome)
            precos.append(preco)
            descricoes.append(descricao)

        for i in range(len(nomes)):
            print(f'Produto: {nomes[i]}\n'
                  f'Preço: {precos[i]}\n'
                  f'Descrição: {descricoes[i]}\n')

        #Salvamos os dados em um arquivo dedicado
        self.salvar_csv(nomes, precos, descricoes)
