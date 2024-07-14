# from playwright.sync_api import Page, BrowserContext, expect
# from pages.pl_softphone_page import PlatformSoftphone
# from pages.login_page import Login
# from pages.kit_softphone_page import KitSoftphone
#
# # ТЕСТ НЕ РАБОТАЕТ В БЕЗГОЛОВОМ РЕЖИМЕ
# class CombinatedPage(Login, KitSoftphone):
#     pass
#
# def test_1(page: Page, context: BrowserContext):
#
#     kit = CombinatedPage(page)
#     kit.full_login()
#     kit.click_icon_softphone()
#     kit.click_keypad()
#     kit.open_caller_id()
#     kit.choose_number_sip()
#     page.locator('.numpad-view__input').fill('+7 901 417-27-47')
#     page2: Page = context.new_page()
#     kit2 = page2
#     kit2.goto('https://kit-eu.preprod.voximplant.xyz/login')
#
#     kit2.locator("[data-type='accept']").click()
#     kit2.get_by_placeholder(" ").nth(0).fill('autopreprod')
#     kit2.get_by_placeholder(" ").nth(1).fill('sromanenko+autopreprod@voximplant.com')
#     kit2.get_by_placeholder(" ").nth(2).fill('Au_962373')
#     kit2.locator("[type='submit']").click()
#     kit2.wait_for_timeout(10000)
#
#     kit.click_to_call_in_softphone()
#
#     kit2.bring_to_front()
#
#
#     kit2.locator('.answer').click()
#     kit2.wait_for_timeout(10000)
#
# # kit2.locator('.sidebar-root-item-icon').nth(1).click()
#     # button_xpath = "//button[@role='button' and text()='Ответить']"
#     # page.locator(button_xpath).click()
#     # kit2.get_by_role('button', name='Ответить').hover()
#     # kit2.get_by_role('button', name='Ответить').click()
#     # kit2.locator('.is-dialing').click()

# ывывамвыамывамвыамывамываывмвыамвамваммывававыа