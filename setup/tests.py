from django.test import LiveServerTestCase
from selenium import webdriver

class AnimaisTestCase(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Chrome('/Users/guilhermelima/Desktop/tdd_busca_animal/chromedriver')

    def tearDown(self):
        self.browser.quit()

    def test_buscando_um_novo_animal(self):
        """
        Teste se um usuário encontra um animal pesquisando
        """
        # Vini, deseja encontrar um novo animal,
        # para adotar.

        # Ele encontra o Busca Animal e decide usar o site,
        home_page = self.browser.get(self.live_server_url + '/')
        # porque ele vê no menu do site escrito Busca Animal.
        brand_element = self.browser.find_element_by_css_selector('.navbar')
        self.assertEqual('Busca Animal', brand_element.text)
        
        # Ele vê um campo para pesquisar animais pelo nome. 
        
        # Ele pesquisa por Leão e clica no botão pesquisar.

        # O site exibe 4 caracteristicas do animal pesquisado.
    
        # Ele desiste de adotar um leão.
        pass
        

