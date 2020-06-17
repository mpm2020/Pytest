class BasePage:
#__init__es lo que se llama como constructor en otros lenguajes OOP como C ++ / Java.
# La idea básica es que es un método especial que se llama automáticamente cuando se crea un objeto de esa clase
#self como sugiere, se refiere a sí mismo , el objeto que ha llamado el método.

    def __init__(self, driver):
        self.driver = driver
        self.base_url = "http://testfaceclub.com/ejercicios"


    def go_to_site(self):
        return self.driver.get(self.base_url)