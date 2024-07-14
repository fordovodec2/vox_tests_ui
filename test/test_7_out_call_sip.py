from playwright.sync_api import Page, BrowserContext, expect
from pages.pl_softphone_page import PlatformSoftphone
from pages.login_page import Login
from pages.kit_softphone_page import KitSoftphone


class CombinatedPage(Login, KitSoftphone):
    pass

def test_call_out_sip(page: Page, context: BrowserContext):

    kit = CombinatedPage(page)
    kit.full_login()
    kit.click_icon_softphone()
    kit.click_keypad()
    kit.open_caller_id()
    kit.choose_number_sip()
    kit.fill_number_sp()
    page2: Page = context.new_page()
    pl_softphone = PlatformSoftphone(page2)
    pl_softphone.full_aut_softphone()
    kit.bring_to_page()
    kit.click_to_call_in_softphone()
    pl_softphone.bring_to_page()
    pl_softphone.answer_call()
    pl_softphone.waiting_10_seconds()
    kit.bring_to_page()
    kit.check_timer_connected()
    pl_softphone.bring_to_page()
    pl_softphone.end_call()
    pl_softphone.click_button_cancel()

