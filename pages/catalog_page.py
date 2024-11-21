from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By

from base.base_class import Base


class CatalogPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    filter_from_100_to_1000 = '//a[contains(text(), "от 100 до 1000")]'
    filter_from_2000_to_5000 = '//a[contains(text(), "от 2000 до 5000")]'
    sort_by_price = '//a[contains(text(), "цене")]'
    product_1 = '(//div[@class="b-category_image"])[1]'
    price_product_1 = '(//span[@class="e-item_price"])[1]'
    buy_product_1 = '(//button[@class="e-item_btn"])[1]'
    product_9 = '(//div[@class="b-item_title"])[9]'
    price_product_9 = '(//span[@class="e-item_price"])[9]'
    buy_product_9 = '(//button[@class="e-item_btn"])[9]'
    cart = '//a[@class="cartico"]'

    # Getters

    def get_filter_from_100_to_1000(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_from_100_to_1000)))

    def get_filter_from_2000_to_5000(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.filter_from_2000_to_5000)))

    def get_sort_by_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.sort_by_price)))

    def get_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_1)))

    def get_price_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_1)))

    def get_buy_product_1(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product_1)))

    def get_product_9(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_9)))

    def get_price_product_9(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.price_product_9)))

    def get_buy_product_9(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.buy_product_9)))

    def get_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart)))

    # Actions

    def click_filter_from_100_to_1000(self):
        self.get_filter_from_100_to_1000().click()
        print('Click filter from 100 to 1000')

    def click_filter_from_2000_to_5000(self):
        self.get_filter_from_2000_to_5000().click()
        print('Click filter from 2000 to 5000')

    def click_sort_by_price(self):
        self.get_sort_by_price().click()
        print('Click sort by price')

    def click_product_1(self):
        self.get_product_1().click()
        print('Click product 1')

    def click_buy_product_1(self):
        self.get_buy_product_1().click()
        print('Click buy product 1')

    def click_buy_product_9(self):
        self.get_buy_product_9().click()
        print('Click buy product 9')

    def click_cart(self):
        self.get_cart().click()
        print('Click cart')

    # Methods

    def select_filter_from_100_to_1000(self):
        self.get_current_url()
        self.click_filter_from_100_to_1000()

    def select_filter_from_2000_to_5000(self):
        self.get_current_url()
        self.click_filter_from_2000_to_5000()

    def select_sort_by_price(self):
        self.get_current_url()
        self.click_sort_by_price()

    def open_product_1(self):
        self.get_current_url()
        self.click_product_1()

    def get_price_product_1_value(self):
        price_product_1 = self.get_price_product_1()
        price_product_1_value = self.get_price_value(price_product_1)
        return price_product_1_value

    def add_product_1_to_cart(self):
        self.get_current_url()
        self.click_buy_product_1()

    def get_price_product_9_value(self):
        price_product_9 = self.get_price_product_9()
        price_product_9_value = self.get_price_value(price_product_9)
        return price_product_9_value

    def add_product_9_to_cart(self):
        self.get_current_url()
        self.click_buy_product_9()

    def select_cart(self):
        self.click_cart()
