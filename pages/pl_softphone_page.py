from playwright.sync_api import Playwright, sync_playwright, expect
from config import *
from pages.general_page import General

class PlatformSoftphone(General):

    def open_platform_sotphone(self):
        self.page.goto(url_softphone)

    def click_button_continue(self):
        self.page.get_by_role('button', name='Continue').click()

    def choose_eng_language(self):
        self.page.locator(".sui-icon.sui-arrow-icon").click()
        self.page.locator("li").filter(has_text="English").click()

    def click_username_field(self):
        self.page.get_by_role('textbox', name='Username').click()

    def fill_username_field(self):
        self.page.get_by_role('textbox', name='Username').fill(username_softphone)

    def click_password_field(self):
        self.page.get_by_role('textbox', name='Password').click()

    def fill_password_field(self):
        self.page.get_by_role('textbox', name='Password').fill(password_softphone)

    def click_ap_name_field(self):
        self.page.get_by_role('textbox', name='Application name').click()

    def fill_ap_name_field(self):
        self.page.get_by_role('textbox', name='Application name').fill(app_name_softphone)

    def click_account_name(self):
        self.page.get_by_role('textbox', name='Account name').click()

    def fill_account_name(self):
        self.page.get_by_role('textbox', name='Account name').fill(acc_name_softphone)

    def click_button_sign_in(self):
        self.page.get_by_role('button', name='Sign in').click()

    def expect_aut_softphone(self):
        expect(self.page.get_by_text('Enter destination', exact=True)).to_be_visible()

    def answer_call(self):
        self.page.locator('.take-call').click()

    def decline_call(self):
        self.page.locator('.close').click()

    def end_call(self):
        self.page.get_by_role('button', name='End call').click()

    def click_button_cancel(self):
        self.page.get_by_role('button', name='Cancel').click()

    def click_field_destination(self):
        self.page.locator('#dialing-input').click()

    def enter_number_ru(self):
        self.page.locator('#dialing-input').fill(number_ru)

    def enter_number_us(self):
        self.page.locator('#dialing-input').fill(number_us)

    def click_button_call(self):

        self.page.get_by_role('button', name='Call', exact=True).click()

    def full_aut_softphone(self):
        self.page.goto(url_softphone)
        self.page.get_by_role('button', name='Continue').click()
        self.page.locator(".sui-icon.sui-arrow-icon").click()
        self.page.locator("li").filter(has_text="English").click()
        self.page.get_by_role('textbox', name='Username').fill(username_softphone)
        self.page.get_by_role('textbox', name='Password').fill(password_softphone)
        self.page.get_by_role('textbox', name='Application name').fill(app_name_softphone)
        self.page.get_by_role('textbox', name='Account name').fill(acc_name_softphone)
        self.page.get_by_role('button', name='Sign in').click()
        expect(self.page.get_by_text('Enter destination', exact=True)).to_be_visible(timeout=15000)

    def full_aut_softphone2(self):
        self.page.goto(url_softphone)
        self.page.get_by_role('button', name='Continue').click()
        self.page.locator(".sui-icon.sui-arrow-icon").click()
        self.page.locator("li").filter(has_text="English").click()
        self.page.get_by_role('textbox', name='Username').fill(username_softphone)
        self.page.get_by_role('textbox', name='Password').fill(password_softphone)
        self.page.get_by_role('textbox', name='Application name').fill(app_name_softphone)
        self.page.get_by_role('textbox', name='Account name').fill(acc_name_softphone)
        self.page.get_by_role('button', name='Sign in').click()
        # expect(self.page.get_by_text('Enter destination', exact=True)).to_be_visible(timeout=15000)
