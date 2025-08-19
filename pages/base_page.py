# pages/base_page.py
import os
from playwright.sync_api import Page
from dotenv import load_dotenv

load_dotenv()

class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = os.getenv("BASE_URL")

    def navigate(self, path=""):
        self.page.goto(f"{self.base_url}{path}")
        self.page.wait_for_load_state("networkidle")
        return self