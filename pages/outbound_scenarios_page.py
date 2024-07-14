from playwright.sync_api import Playwright, sync_playwright, expect
from pages.general_page import General
from config import *

class OutboundScenarios(General):

    def open_page_outbound(self):
        self.page.goto(f'{host}/Outbound/Scenarios', wait_until='domcontentloaded')

    def open_outbound_scenarios(self):

        self.page.locator('.sidebar-root-item-icon').nth(0).click()
        self.page.locator('[href="/Outbound"]').click()
        expect(self.page).to_have_url(f'{host}/Outbound/Scenarios')

    def click_add_scenario(self):

        self.page.locator('.template-gallery-btn__create').click()

    def check_new_scenario_is_delete(self):

        expect(self.page.get_by_text(new_out_scenario, exact=True)).to_be_hidden()

    def check_page_outbound_scenarios(self):

        expect(self.page).to_have_url(f'{host}/Outbound/Scenarios')

    def check_name_new_out_scenario(self):

        self.page.get_by_text(new_out_scenario, exact=True).hover()

    def click_rename_scenario(self):
        self.page.locator(".option-popup>li:nth-child(1)").click()

    def click_duplicate_scenario(self):
        self.page.locator(".option-popup>li:nth-child(2)").click()

    def click_move_scenario(self):
        self.page.locator(".option-popup>li:nth-child(3)").click()

    def click_open_new_tab_scenario(self):
        self.page.locator(".option-popup>li:nth-child(2)").click()

    def click_delete_scenario(self):
        self.page.locator('.option-popup>.is-active-delete').click()

    def click_confirm_delete_scenario(self):
        self.page.locator('.kit-btn.is-default').click()









