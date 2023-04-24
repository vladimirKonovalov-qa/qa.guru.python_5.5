import pytest
from selene import browser
import os

@pytest.fixture(scope='function', autouse=True)
def browser_action():
    browser.open('https://demoqa.com/automation-practice-form')