# Trabalho Prático Selenium - Grupo 3 

### Colaboradores: 
- João Pedro Rodrigues da Silva
- Mateus Arantes Novaes 

### Sobre o projeto
O presente repositório armazena todos os arquivos da atividade de automatização de Web Scraping com Selenium, proposto para os trainees da Pi Junior. 

A ideia geral do projeto é automatizar a interação com o site Swag Labs (ou SauceDemo -- disponível em: "https://www.saucedemo.com/") um e-commerce de demonstração, utilizando SeleniumBase para a automação. 

### Objetivos
- Realizar o **login automatizado** no site.
- Extrair as **informações dos produtos** disponíveis na loja. Além disso, buscou-se armazenar todos as informações coletadas nesse processo em um arquivo do tipo **.csv**. 
- Automatizar todo o processo de **compra**, adicionando todos os produtos ao carrinho de compras do site  e **realizando** o pedido.
- Realizar a "raspagem" da **mensagem de confirmação** e da **forma de entrega** e **método de pagamento**. Além disso, a **mensagem de confirmação** do pedido também foi coletada. 

#### Estrutura geral do projeto: 
- O diretório 'data' armazena o arquivo csv que armazena as informações coletadas durante a execução do script com Selenium.
- O diretório 'src' armazena os arquivos .py com os módulos que executam cada tarefa de interação com o site explorado, além do arquivo 'main.py' que importa e executa cada uma das funções, testando a execução.
- Cada módulo é nomeado de forma autoexplicativa (por exemplo, o módulo 'adicionar_ao_carrinho' contêm a função que adiciona todos os produtos disponíveis ao carrinho de compras do site), visando uma maior legibilidade dos arquivos do projeto. 
