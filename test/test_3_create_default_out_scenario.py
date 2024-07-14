# Тест создает дефолтный исходящий сценарий
from playwright.sync_api import Page, BrowserContext, expect
from pages.outbound_scenarios_page import OutboundScenarios
from pages.login_page import Login

def test_create_out_scenario(page: Page, context: BrowserContext):
    out = OutboundScenarios(page)
    out.open_page_outbound()
    out.open_outbound_scenarios()
    out.waiting_10_seconds()
    out.click_add_scenario()
    out.rename_out_scenario_in_editor()
    out.click_publish_in_editor()
    out.add_description_to_scenario_in_editor()
    out.click_publish_in_editor_modal()
    out.click_editor_logo()
    out.check_page_outbound_scenarios()
    out.check_name_new_out_scenario()
    out.click_action_menu_new_scenario()
    out.click_delete_scenario()
    out.click_confirm_delete_scenario()
    out.check_new_scenario_is_delete()


