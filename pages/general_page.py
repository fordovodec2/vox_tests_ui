from playwright.sync_api import Playwright, sync_playwright, expect
from config import *

class General:
    def __init__(self, page):
        self.page = page

    def bring_to_page(self):
        self.page.bring_to_front()

    def waiting_10_seconds(self):
        self.page.wait_for_timeout(10000)

    def waiting_15_seconds(self):
        self.page.wait_for_timeout(15000)

    def click_button_answer_inbound(self):
        self.page.locator('.answer').click()

    def expect_timer_wrapper_block(self):
        expect(self.page.locator('.timer.f_12_regular')).to_be_visible()

    def full_login_from_general(self):
        self.page.goto(url)
        self.page.locator("[data-type='accept']").click()
        self.page.get_by_placeholder(" ").nth(0).fill(domain)
        self.page.get_by_placeholder(" ").nth(1).fill(mail)
        self.page.get_by_placeholder(" ").nth(2).fill(password)
        self.page.locator("[type='submit']").click()
        expect(self.page.locator('.header-hero.agent-status-wrap')).to_be_visible(timeout=20000)

    def check_url_outbound_scenarios(self):
        expect(self.page).to_have_url(f'{host}/Outbound/Scenarios')

    def rename_out_scenario_in_editor(self):
        self.page.locator('.editor-panel--logo').click()
        self.page.get_by_placeholder(" ").click(click_count=3)
        self.page.get_by_placeholder(" ").fill(new_out_scenario)

    def rename_inb_scenario_in_editor(self):
        self.page.locator('.editor-panel--logo').click()
        self.page.get_by_placeholder(" ").click(click_count=3)
        self.page.get_by_placeholder(" ").fill(new_inb_scenario)

    def click_publish_in_editor(self):
        self.page.locator('.editor-panel>[type="button"]').click()

    def click_publish_in_editor_modal(self):
        self.page.locator('.dialog-footer>[type="button"]').nth(0).click()

    def click_editor_logo(self):
        self.page.locator('.editor-logo').click()

    def add_description_to_scenario_in_editor(self):
        self.page.get_by_role('textbox').click()
        self.page.get_by_role('textbox').fill('For autotests')

    def click_action_menu_new_scenario(self):
        self.page.locator('.file__more').nth(0).click()

    def close_modal_window(self):
        """Метод закрывается модальное окно "Что нового?" если оно есть"""
        if self.page.locator('.kit-modal__close').is_visible():
            self.page.locator('.kit-modal__close').click()

    def agree_modal_window(self):
        """Метод нажимает "Понятно" в модальном окне "Что нового?" если оно есть"""
        self.page.wait_for_timeout(15000)
        if self.page.locator('.modal-change-notification_footer>[type="button"]').is_visible():
            self.page.locator('.modal-change-notification_footer>[type="button"]').click()

    def page_outbound_scenarios(self):
        self.page.goto(f'{host}/Outbound/Scenarios', wait_until='domcontentloaded')
