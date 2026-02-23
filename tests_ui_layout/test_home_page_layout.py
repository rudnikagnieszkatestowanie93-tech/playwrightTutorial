from playwright.sync_api import expect
from pom.home_page_element import HomePage
from pom.shop_women_elements import ShopWomen
import pytest

@pytest.mark.smoke
@pytest.mark.parametrize('page', [])
def pytes(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    home_page = HomePage(page)
    shop_women = ShopWomen(page)

    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()

@pytest.mark.integration
def test_about_us_section_2(page):
    page.goto("https://symonstorozhenko.wixsite.com/website-1")

    home_page = HomePage(page)
    shop_women = ShopWomen(page)

    expect(home_page.celebrate_header).to_be_visible()
    expect(home_page.celebrate_body).to_be_visible()

    expect(shop_women.celebrating_beauty_header).to_be_visible()
    expect(shop_women.celebrating_beauty_body).to_be_visible()







