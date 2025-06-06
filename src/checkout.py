from seleniumbase import BaseCase

class Checkout(BaseCase):
    def preencher_formulario_checkout(self):
        #Clicando no botão de checkout
        self.click("#checkout")

        # Espera os campos do formulário serem carregados
        self.wait_for_element("#first-name")

        #Preenchendo o formulário
        self.type("#first-name", "Trainee")
        self.type("#last-name", "PiJunior")
        self.type("#postal-code", "31270-901")

        #Clicando no botão de continuar
        self.click("#continue")
