from seleniumbase import BaseCase

class LoginSauceDemo(BaseCase):
    def login(self):
        #Abrir o navegador
        self.open("https://www.saucedemo.com/")

        #Digitando as credenciais
        self.type("#user-name" ,"standard_user")
        self.type("#password", "secret_sauce")

        #Interagindo com o botão de login
        self.click("#login-button")

        # Espera explícita para garantir que a página de produtos carregue completamente
        self.wait_for_element(".inventory_list")
