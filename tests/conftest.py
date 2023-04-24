import pytest
from selene import browser


@pytest.fixture(scope='function', autouse=True)
def browser_action():
    browser.config.base_url = 'https://demoqa.com'