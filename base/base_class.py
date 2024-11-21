import datetime
import re

from selenium.webdriver.common.by import By


class Base:

    def __init__(self, driver):
        self.driver = driver


    '''Method get current url'''

    def get_current_url(self):
        get_url = self.driver.current_url
        print('Current url ' + get_url)


    '''Method assert word'''

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Good value word')

    '''Method screenshot'''

    def get_screenshot(self):
        now_date = datetime.datetime.now().strftime("%Y.%m.%d.%H.%M.%S")
        name_screenshot = 'screenshot' + now_date + '.png'
        self.driver.save_screenshot('C:\\Users\\user\\PycharmProjects\\ural_project\\screen\\' + name_screenshot)

    '''Method assert url'''

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print('Good value url')

    '''Method get price'''

    def get_price_value(self, price):
        price_value = int(re.sub(r'\D', '', price.text))
        print(price_value)
        return price_value

    '''Method assert price'''

    def assert_price(self, price_1, price_2):
        assert price_1 == price_2
        print('Good value price')

    '''Scroll down'''
    def scroll_down(self, point):
        self.driver.execute_script(f"window.scrollTo(0, {point})")

    '''Scroll up'''

    def scroll_up(self):
        self.driver.execute_script("window.scrollTo(0, -500)")


    '''Click on body'''
    def click_on_body(self):
        self.driver.find_element(By.TAG_NAME, "body").click()