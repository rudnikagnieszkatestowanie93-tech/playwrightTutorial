# import time
# from playwright.sync_api import Playwright, sync_playwright
# import pytest
#
# from conf_test import set_up, login_set_up
#
#
# @pytest.mark.smoke
# @pytest.mark.regression
# def test_login(playwright: Playwright)->None:
#
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://symonstorozhenko.wixsite.com/website-1")
#     page.set_default_timeout(3000)
