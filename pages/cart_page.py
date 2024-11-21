from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from base.base_class import Base


class CartPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators

    common_price = '(//span[@class="bs"])[1]'
    name = '//input[@name="name"]'
    phone = '//input[@id="phone"]'
    city = '//input[@name="city"]'
    street = '//input[@name="str"]'
    building = '//input[@name="building"]'
    finish_button = '//button[@name="ordering"]'

    # Getters

    def get_common_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.common_price)))

    def get_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name)))

    def get_phone(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.phone)))

    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.city)))

    def get_street(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.street)))

    def get_building(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.building)))

    def get_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.finish_button)))

    # Actions

    def input_name(self, name):
        self.get_name().send_keys(name)
        print('Input name')

    def input_phone(self, phone):
        self.get_phone().click()
        for char in phone:
            ActionChains(self.driver).send_keys(char).perform()
        print('Input phone')

    def input_city(self, city):
        self.get_city().send_keys(city)
        print('Input city')

    def input_street(self, street):
        self.get_street().send_keys(street)
        print('Input street')

    def input_building(self, building):
        self.get_building().send_keys(building)
        print('Input building')

    def click_finish_button(self):
        self.get_finish_button().click()
        print('Click finish button')

    # Methods

    def get_common_price_value(self):
        price_product = self.get_common_price()
        price_product_value = self.get_price_value(price_product)
        return price_product_value

    def input_information(self):
        self.get_current_url()
        self.input_name('Михаил')
        self.input_phone('9999999999')
        self.input_city('Москва')
        self.input_street('Садовая')
        self.input_building('14')
        """Без клика, т.к. клик приводит к оформлению заказа"""
        #self.click_finish_button()