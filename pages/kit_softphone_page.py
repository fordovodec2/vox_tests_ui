from playwright.sync_api import Playwright, sync_playwright, expect
# from config.stand import *
from config import *
from pages.general_page import General
ICON_SOFTPHONE = '.sc-icon.sp-button__icon'
LIST_CALLERID = '.callerid-picker__picked-number'
ENTRY_FIELD_NUMBER = '.numpad-view__input'
BUTTON_ICON_PHONE = '.call-btn__wrapper'
class KitSoftphone(General):

    def click_icon_softphone(self):
        self.page.locator(ICON_SOFTPHONE).click()

    def click_keypad(self):
        self.page.locator("header").get_by_role("button").nth(3).click()

    def open_caller_id(self):
        self.page.locator(LIST_CALLERID).click()

    def choose_number_ru(self):

        self.page.get_by_text(number_ru).nth(1).click()
    # ВНИМАНИЕ! метод choose_number_ru сработает, если в каллер айди уже выбран такой номер.
    # такое происходит если номер выбран по умолчанию и его же нужно выбрать из списка
    # чтобы выбрать другие номера, отличные от того, что уже выбран нужно убрать nth(1)

    def choose_number_us(self):
        self.page.get_by_text(number_us).click()

    def choose_number_sip(self):
        self.page.get_by_text(number_sip).click()

    def fill_number_sp(self):
        self.page.locator(ENTRY_FIELD_NUMBER).fill(number_sp)

    def click_to_call_in_softphone(self):
        self.page.locator(BUTTON_ICON_PHONE).click()

    def check_timer_connected(self):
        expect(self.page.locator('.call-dialog__timer.connected')).to_be_visible()

