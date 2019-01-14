from selenium.webdriver.common.by import By

from .base_element import BaseElement
from .base_page import BasePage
from .locator import Locator


class TrialPage(BasePage):

    url = 'https://techstepacademy.com/trial-of-the-stones'

    @property
    def stone_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#r1Input')
        return BaseElement(self.driver, locator)

    @property
    def stone_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='button#r1Btn')
        return BaseElement(self.driver, locator)

    @property
    def secrets_input(self):
        locator = Locator(by=By.CSS_SELECTOR, value='input#r2Input')
        return BaseElement(self.driver, locator)

    @property
    def secrets_button(self):
        locator = Locator(by=By.CSS_SELECTOR, value='button#r2Btn')
        return BaseElement(self.driver, locator)
