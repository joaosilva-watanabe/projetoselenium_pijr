from seleniumbase import BaseCase

class LoginSauceDemo(BaseCase):
    def login(self):
        #Abrir o navegador
        self.open("https://www.saucedemo.com/")

        #Digitando as credenciais
        self.type("#Username" ,"standard_user")
        self.type("#Password", "secret_sauce")

        #Interagindo com o botão de login
        self.click("#login-button")
