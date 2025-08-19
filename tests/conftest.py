# tests/conftest.py
import json
import os

import pytest
from playwright.async_api import Page

from pages.page_factory import PageFactory

@pytest.fixture(scope="session")
def test_data():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_path = os.path.join(project_root, "data", "test_data.json")
    with open(data_path, encoding="utf-8") as f:
        return json.load(f)

@pytest.fixture
def home_page(page: Page):
    home = PageFactory.get_page("home", page).navegar()
    return home