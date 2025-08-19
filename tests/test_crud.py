# tests/test_crud.py
import json
import os

import pytest
from playwright.sync_api import Page

# Obtém o caminho absoluto do diretório do projeto
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(PROJECT_ROOT, "data", "test_data.json")

# Carrega os dados de teste do arquivo JSON
with open(DATA_PATH, encoding="utf-8") as f:
    test_data = json.load(f)

@pytest.mark.create
def test_cadastrar_novo_usuario(home_page, test_data):
    print("\n--- Executando o Teste de Cadastro (Create) ---")

    home_page.preencher_form_e_enviar(test_data["usuario_cadastro"])

    assert home_page.page.url == "https://demo.automationtesting.in/Register.html"
    print("O formulário foi preenchido e submetido com sucesso.")


@pytest.mark.skip(reason="Teste exemplo de edição, a aplicação web não possui funcionalidade.")
@pytest.mark.update
def test_editar_usuario_existente(page: Page):
    print("\n--- Executando o Teste de Edição (Update) - Cenário Hipotético ---")
    print("Teste de Edição (hipotético) concluído.")


@pytest.mark.skip(reason="Teste exemplo de deleção, a aplicação web não possui funcionalidade.")
@pytest.mark.delete
def test_deletar_usuario_existente(page: Page):
    print("\n--- Executando o Teste de Deleção (Delete) - Cenário Hipotético ---")
    print("Teste de Deleção (hipotético) concluído.")