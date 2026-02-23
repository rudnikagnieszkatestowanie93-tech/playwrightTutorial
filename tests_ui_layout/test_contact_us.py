import pytest
from playwright.sync_api import expect
from pom.contact_us_page import ContactUsPage

@pytest.mark.regression
def test_submit_form(page):

    contact_us = ContactUsPage(page)

    contact_us.navigate()

    contact_us.submit_form(
        "Symon",
        "123 Main",
        "test@email.com",
        "123-456-1213",
        "test subject",
        "balkbala"
    )