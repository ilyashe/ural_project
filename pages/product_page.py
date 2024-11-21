from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from base.base_class import Base


class ProductPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    select_size = '//select[@id="size"]'
    price_product = '(//div[@class="b-item_price"])[1]'
    buy_product = '(//button[@class="e-slider_btn"])[1]'

    # Getters

    def get_select_size(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_size)))

    def get_price_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product)))

    def get_buy_product(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product)))

    # Actions

    def select_size_xl(self):
        select = Select(self.get_select_size())
        select.select_by_visible_text('XL')
        print('Click select size XL')

    def click_buy_product(self):
        self.get_buy_product().click()
        print('Click buy product')

    # Methods

    def get_price_product_value(self):
        price_product = self.get_price_product()
        price_product_value = self.get_price_value(price_product)
        return price_product_value

    def add_product_xl_to_cart(self):
        self.get_current_url()
        self.select_size_xl()
        self.click_buy_product()
