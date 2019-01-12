from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage


class TrialPage(BasePage):

    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def stone_input(self):
        locator = (By.CSS_SELECTOR, 'input#r1Input')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def stone_button(self):
        locator = (By.CSS_SELECTOR, 'button#r1Btn')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def secrets_input(self):
        locator = (By.CSS_SELECTOR, 'input#r2Input')
        return BaseElement(self.driver, by=locator[0], value=locator[1])

    @property
    def secrets_button(self):
        locator = (By.CSS_SELECTOR, 'button#r2Btn')
        return BaseElement(self.driver, by=locator[0], value=locator[1])
