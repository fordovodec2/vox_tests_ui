from playwright.sync_api import Page, BrowserContext
from pages.login_page import Login

# def test_login(page: Page, context: BrowserContext):
#     login_page = Login(page)
#     login_page.open()
#     login_page.accept_button_click()
#     login_page.domain_field_click()
#     login_page.domain_fill()
#     login_page.mail_field_click()
#     login_page.mail_fill()
#     login_page.password_field_clik()
#     login_page.password_fill()
#     login_page.button_sign_in_click()
#     login_page.close_modal_window()
#     login_page.expecting_agent_status_block()
