from playwright.sync_api import Page, BrowserContext
from pages.pl_softphone_page import PlatformSoftphone


def test_pl_softphone(page: Page, context: BrowserContext):
    pl_softphone = PlatformSoftphone(page)
    pl_softphone.open_platform_sotphone()
    pl_softphone.click_button_continue()
    pl_softphone.choose_eng_language()
    pl_softphone.fill_username_field()
    pl_softphone.fill_password_field()
    pl_softphone.fill_ap_name_field()
    pl_softphone.fill_account_name()
    pl_softphone.click_button_sign_in()
    pl_softphone.expect_aut_softphone()
