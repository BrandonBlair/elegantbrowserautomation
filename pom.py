class TrainingGroundPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://techstepacademy.com/training-ground/'

    def go(self):
        self.driver.get(self.url)
    
    def type_into_input(self, text):
        inpt = self.driver.find_element_by_id('ipt1')
        inpt.clear()
        inpt.send_keys(text)
        return None
    
    def get_input_text(self):
        inpt = self.driver.find_element_by_id('ipt1')
        elem_text = inpt.get_attribute('value')
        return elem_text

    def click_button_1(self):
        button = self.driver.find_element_by_id('b1')
        button.click()
        return None


# Our Test
from selenium import webdriver

# Test Setup
browser = webdriver.Chrome()
test_value = 'it worked'

# Test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_into_input(test_value)
#trng_page.click_button_1()
txt_from_input = trng_page.get_input_text()
assert txt_from_input == test_value, f"Test Failed: Input did not match expected {test_value}."
print("Test Passed.")