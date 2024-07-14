# Данный тест проверяет входящий звонок по ПСТН на кит из платформенного софтфона
# Условия: На тестируемом аккаунте должен быть сценарий, в котором есть блок добавочный, чтобы позвонить оператору
from playwright.sync_api import Page, BrowserContext, expect
from pages.pl_softphone_page import PlatformSoftphone
from pages.login_page import Login
from pages.kit_softphone_page import KitSoftphone

def test_inbound_pstn(page: Page, context: BrowserContext):

    kit_in = KitSoftphone(page)
    kit_in.page_outbound_scenarios()
    page2:  Page = context.new_page()
    pl_softphone = PlatformSoftphone(page2)
    pl_softphone.full_aut_softphone2()
    # pl_softphone.waiting_10_seconds()
    pl_softphone.click_field_destination()
    pl_softphone.enter_number_ru()
    pl_softphone.click_button_call()
    kit_in.bring_to_page()
    kit_in.click_button_answer_inbound()
    # kit_in.waiting_15_seconds()
    kit_in.expect_timer_wrapper_block()



