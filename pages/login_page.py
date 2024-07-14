from playwright.sync_api import Playwright, sync_playwright, expect
from pages.general_page import General
from config import *
BUTTON_ACCEPT_ALL_COOKIES = "[data-type='accept']"
BUTTON_SIGN_IN = "[type='submit']"

class Login(General):

    def open(self):
        self.page.goto(url)

    def accept_button_click(self):
        self.page.locator(BUTTON_ACCEPT_ALL_COOKIES).click()

    def domain_field_click(self):
        self.page.get_by_placeholder(" ").nth(0).click()

    def domain_fill(self):
        self.page.get_by_placeholder(" ").nth(0).fill(domain)

    def mail_field_click(self):
        self.page.get_by_placeholder(" ").nth(1).click()

    def mail_fill(self):
        self.page.get_by_placeholder(" ").nth(1).fill(mail)

    def password_field_clik(self):
        self.page.get_by_placeholder(" ").nth(2).click()

    def password_fill(self):
        self.page.get_by_placeholder(" ").nth(2).fill(password)

    def button_sign_in_click(self):
        self.page.locator(BUTTON_SIGN_IN).click()

    def expecting_agent_status_block(self):
        expect(self.page.locator('.header-hero.agent-status-wrap')).to_be_visible(timeout=20000)

    def full_login(self):

        self.page.goto(url)
        self.page.locator(BUTTON_ACCEPT_ALL_COOKIES).click()
        self.page.get_by_placeholder(" ").nth(0).fill(domain)
        self.page.get_by_placeholder(" ").nth(1).fill(mail)
        self.page.get_by_placeholder(" ").nth(2).fill(password)
        self.page.locator(BUTTON_SIGN_IN).click()
        expect(self.page.locator('.header-hero.agent-status-wrap')).to_be_visible(timeout=20000)
