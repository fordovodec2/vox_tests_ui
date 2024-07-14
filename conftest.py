
from pages.login_page import Login
from typing import Generator
import pytest
from playwright.sync_api import Page, BrowserContext, Playwright

@pytest.fixture(scope='session')
def login(browser):
    context: BrowserContext = browser.new_context()
    page = context.new_page()

    login_page = Login(page)
    login_page.open()
    login_page.accept_button_click()
    login_page.domain_fill()
    login_page.mail_fill()
    login_page.password_fill()
    login_page.button_sign_in_click()
    login_page.agree_modal_window()
    login_page.expecting_agent_status_block()
    context.storage_state(path="state.json")
    context.close()
    browser.close()

@pytest.fixture()
def context(playwright, login):
    # browser = playwright.chromium.launch(headless=False, args=["--headless=new"]) - МИКРОФОН !!!! это работает
    browser = playwright.chromium.launch(headless=False)
    context: BrowserContext = browser.new_context(permissions=["microphone"], storage_state="state.json")

    yield context
    context.close()
    browser.close()

@pytest.fixture()
def page(context: BrowserContext):
    page: Page = context.new_page()
    # page.set_viewport_size({'height': 800, 'width': 1400})
    yield page
    page.close()

# -________________________Криво работающие фикстуры для файрфокс____________________-
# @pytest.fixture(scope="session")
# def context(playwright: Playwright) -> Generator[BrowserContext, None, None]:
#     browser = playwright.firefox.launch(
#         headless=True,
#         args=[
#             '--use-fake-ui-for-media-stream',  # Использование поддельного UI для медиа-потока
#             '--use-fake-device-for-media-stream'  # Использование поддельных медиа-устройств
#         ],
#         firefox_user_prefs={
#             "media.navigator.permission.disabled": True,  # Отключение запроса разрешений
#             "media.navigator.streams.fake": True  # Использование поддельных потоков медиа
#         }
#     )
#
#     context: BrowserContext = browser.new_context()
#     yield context
#     context.close()
#     browser.close()
#
#
# @pytest.fixture()
# def page(context: BrowserContext) -> Generator[Page, None, None]:
#     page = context.new_page()
#     yield page
#     page.close()