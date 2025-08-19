# Projeto de automação de testes web com Playwright + Cucumber (BDD)

Projeto de automação de testes web com Playwright + Cucumber (BDD), este projeto utiliza TypeScript.

## Pré-requisitos

- Node.js 18+
- npm

## Instalação

```bash
npm install
```
## Instale as dependências listadas no arquivo requirements.txt:
```bash
pip install -r requirements.txt
```
## Instale os navegadores que o Playwright usará para rodar os testes:
```bash
playwright install
```

## Execução dos testes
```bash
pytest
```

```bash -Execução com interface gráfica (para visualização):
pytest --headed
```

```bash - Execução com logs detalhados:
pytest -s
```

## Estrutura do projeto
.
├── .gitignore              # Ignora arquivos e pastas que não devem ser versionados (ex: venv/)
├── pages/                  # Contém os Page Object Models (POMs) para organizar elementos e métodos da página
│   ├── base_page.py
│   ├── __init__.py         # Torna a pasta 'pages' um pacote Python
│   ├── page_factory.py     # Cria e gerencia as instâncias das páginas
│   └── home_page.py
├── tests/                  # Contém os arquivos de teste
│   ├── __init__.py         # Torna a pasta 'tests' um pacote Python
│   ├── conftest.py         # Arquivo para fixtures e configurações de teste (ex: page_factory)
│   └── test_crud.py
├── requirements.txt        # Lista as dependências do projeto
└── README.md               # Este arquivo de documentação