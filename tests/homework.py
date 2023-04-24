from selene import browser
from selene import be, have
import os


def test_registration_form():
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('IvanovIvan@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('+990989968')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="6"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1990"]').click()
    browser.element('[aria-label="Choose Tuesday, July 3rd, 1990"]').click()
    browser.element('#subjectsInput').type('English').press_enter().type('Commerce').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd()+'tests/resources/agggg.jpg')

    browser.element('#currentAddress').type('163 McGlynn Crossroad North Madonnachester, VIC 2092')




