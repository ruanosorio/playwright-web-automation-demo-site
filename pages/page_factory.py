# pages/page_factory.py
from playwright.sync_api import Page
from pages.home_page import HomePage


class PageFactory:
    @staticmethod
    def get_page(page_name, page: Page):
        if page_name == "home":
            return HomePage(page)

        # Adicione mais páginas aqui conforme necessário
        # elif page_name == "login":
        #    return LoginPage(page)

        else:
            raise ValueError(f"Página desconhecida: {page_name}")