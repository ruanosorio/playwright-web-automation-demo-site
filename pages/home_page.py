# pages/home_page.py
from pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.url_path = "Register.html"

        #Locators

        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.address_input = page.locator("textarea[ng-model='Adress']")
        self.email_input = page.locator("input[type='email']")
        self.phone_input = page.locator("input[type='tel']")
        self.gender_radio = lambda gender: page.get_by_text(gender, exact=True)
        self.hobbies_checkbox = lambda hobby: page.locator(f"input[type='checkbox'][value='{hobby}']")
        self.language_select = page.locator("#msdd")
        self.skills_select = page.locator("#Skills")
        self.country_select = page.locator("span[role='combobox']")
        self.year_select = page.locator("#yearbox")
        self.month_select = page.locator("select[ng-model='monthbox']")
        self.day_select = page.locator("#daybox")
        self.password_input = page.locator("#firstpassword")
        self.confirm_password_input = page.locator("#secondpassword")

        self.submit_button = page.get_by_role("button", name="Submit")
        self.refresh_button = page.get_by_role("button", name="Refresh")

    def navegar(self):
        self.navigate(self.url_path)
        return self

    def preencher_primeiro_nome(self, nome):
        self.first_name_input.fill(nome)
        return self

    def preencher_sobrenome(self, sobrenome):
        self.last_name_input.fill(sobrenome)
        return self

    def preencher_endereco(self, endereco):
        self.address_input.fill(endereco)
        return self

    def preencher_email(self, email):
        self.email_input.fill(email)
        return self

    def preencher_telefone(self, telefone):
        self.phone_input.fill(telefone)
        return self

    def selecionar_genero(self, genero):
        self.gender_radio(genero).check()
        return self

    def selecionar_hobbies(self, hobbies):
        for hobby in hobbies:
            self.hobbies_checkbox(hobby).check()
        return self


    def selecionar_idiomas(self, idiomas):
        #Clica no campo para abrir a lista de idiomas
        self.language_select.click()

        # Navega a lista de idiomas para selecionar cada um
        for idioma in idiomas:
            idioma_locator = self.page.get_by_text(idioma, exact=True)
            # Espera que o elemento da lista esteja visível e depois clica
            idioma_locator.wait_for(state="visible")
            idioma_locator.click()

        # Clica novamente no campo para fechar a lista após selecionar a opção
        self.language_select.click()

        return self

    def selecionar_habilidade(self, habilidade):
        self.skills_select.select_option(habilidade)
        return self

    def selecionar_pais(self, pais):
        self.country_select.click()
        self.page.get_by_role("textbox").fill(pais)
        self.page.keyboard.press("Enter")
        return self

    def selecionar_data_nascimento(self, ano, mes, dia):
        self.year_select.select_option(ano)
        self.month_select.select_option(mes)
        self.day_select.select_option(dia)
        return self

    def preencher_senha(self, senha, confirmar_senha):
        self.password_input.fill(senha)
        self.confirm_password_input.fill(confirmar_senha)
        return self

    def clicar_enviar(self):
        self.submit_button.click()
        self.page.wait_for_timeout(3000)
        return self

    def preencher_form_e_enviar(self, dados_usuario):
        self.preencher_primeiro_nome(dados_usuario["first_name"]) \
            .preencher_sobrenome(dados_usuario["last_name"]) \
            .preencher_endereco(dados_usuario["address"]) \
            .preencher_email(dados_usuario["email"]) \
            .preencher_telefone(dados_usuario["phone"]) \
            .selecionar_genero(dados_usuario["gender"]) \
            .selecionar_hobbies(dados_usuario["hobbies"]) \
            .selecionar_habilidade(dados_usuario["skill"]) \
            .selecionar_data_nascimento(
            dados_usuario["dob"]["year"],
            dados_usuario["dob"]["month"],
            dados_usuario["dob"]["day"]
        ) \
            .preencher_senha(dados_usuario["password"], dados_usuario["confirm_password"]) \
            .clicar_enviar()