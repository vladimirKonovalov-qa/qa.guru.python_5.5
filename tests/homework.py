from selene import browser
from selene import have, command
import os


def test_registration_form():
    browser.open('/automation-practice-form')
    browser.element('#firstName').type('Ivan')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('IvanovIvan@mail.ru')
    browser.element('#gender-radio-1').double_click()
    browser.element('#userNumber').type('1990989968')
    browser.element('#dateOfBirthInput').click()
    browser.element('[class="react-datepicker__month-select"]').click().element('[value="6"]').click()
    browser.element('[class="react-datepicker__year-select"]').click().element('[value="1990"]').click()
    browser.element('[aria-label="Choose Tuesday, July 3rd, 1990"]').click()
    browser.element('#subjectsInput').type('English').press_enter().type('Commerce').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('#uploadPicture').send_keys(os.getcwd()+'/resources/agggg.jpg')
    browser.element('#currentAddress').type('163 McGlynn Crossroad North Madonnachester, VIC 2092')
    browser.element('#react-select-3-input').type('NCR').press_enter()
    browser.element('#react-select-4-input').type('Delhi').press_enter()
    browser.element('#submit').perform(command.js.scroll_into_view)
    browser.element('#submit').press_enter()

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('.table td:nth-child(2)').should(have.exact_texts(
        'Ivan Ivanov',
        'IvanovIvan@mail.ru',
        'Male',
        '1990989968',
        '03 July,1990',
        'English, Commerce',
        'Sports',
        'agggg.jpg',
        '163 McGlynn Crossroad North Madonnachester, VIC 2092',
        'NCR Delhi'))





