from pages.swag_labs import SwagLabs


def test_swag(browser):
    testswag = SwagLabs(browser)
    testswag.visit()
    testswag.exist_icon()


def test_swag2(browser):
    testswag = SwagLabs(browser)
    testswag.visit()
    testswag.find_element('#user-name')


def test_swag3(browser):
    testswag = SwagLabs(browser)
    testswag.visit()
    testswag.find_element('#password')

